"""
The Node Discovery protocol provides a way to find RLPx nodes that can be connected to. It uses a
Kademlia-like protocol to maintain a distributed database of the IDs and endpoints of all
listening nodes.

More information at https://github.com/ethereum/devp2p/blob/master/rlpx.md#node-discovery
"""
import asyncio
import logging
import time
from typing import (
    Any,
    AnyStr,
    Callable,
    Generator,
    List,
    Tuple
)

import rlp
from eth_utils import (
    decode_hex,
    force_bytes,
    to_list,
)

from eth_keys import keys
from eth_keys import datatypes

import kademlia
from evm.utils.keccak import keccak
from evm.utils.numeric import (
    big_endian_to_int,
    int_to_big_endian,
    safe_ord,
)
import bootstrap
import crawlerdb

# UDP packet constants.
MAC_SIZE = 256 // 8  # 32
SIG_SIZE = 520 // 8  # 65
HEAD_SIZE = MAC_SIZE + SIG_SIZE  # 97
EXPIRATION = 60  # let messages expire after N secondes
PROTO_VERSION = 4


class DefectiveMessage(Exception):
    pass


class WrongMAC(DefectiveMessage):
    pass


class Command():
    def __init__(self, name: str, id: int, elem_count: int) -> None:
        self.name = name
        self.id = id
        # Number of required top-level list elements for this cmd.
        # Elements beyond this length must be trimmed.
        self.elem_count = elem_count

    def __repr__(self):
        return 'Command(%s:%d)' % (self.name, self.id)


CMD_PING = Command("ping", 1, 4)
CMD_PONG = Command("pong", 2, 3)
CMD_FIND_NODE = Command("find_node", 3, 2)
CMD_NEIGHBOURS = Command("neighbours", 4, 2)
CMD_ID_MAP = dict((cmd.id, cmd) for cmd in [CMD_PING, CMD_PONG, CMD_FIND_NODE, CMD_NEIGHBOURS])


class DiscoveryProtocol(asyncio.DatagramProtocol):
    """A Kademlia-like protocol to discover RLPx nodes."""
    logger = logging.getLogger("evm.p2p.discovery.DiscoveryProtocol")
    transport = None  # type: asyncio.DatagramTransport
    _max_neighbours_per_packet_cache = None

    def __init__(self, privkey: datatypes.PrivateKey, address: kademlia.Address,
                 bootstrap_nodes: List[kademlia.Node]) -> None:
        self.privkey = privkey
        self.address = address
        self.bootstrap_nodes = bootstrap_nodes
        self.this_node = kademlia.Node(self.pubkey, address)
        self.kademlia = kademlia.KademliaProtocol(self.this_node, wire=self)
        
        # This is my stuff now
        self.mydb = crawlerdb.CrawlerDb()

    @property
    def pubkey(self) -> datatypes.PublicKey:
        return self.privkey.public_key

    def _get_handler(self, cmd) -> Callable[[kademlia.Node, List[Any], AnyStr], None]:
        if cmd == CMD_PING:
            return self.recv_ping
        elif cmd == CMD_PONG:
            return self.recv_pong
        elif cmd == CMD_FIND_NODE:
            return self.recv_find_node
        elif cmd == CMD_NEIGHBOURS:
            return self.recv_neighbours
        else:
            raise ValueError("Unknwon command: {}".format(cmd))

    def _get_max_neighbours_per_packet(self):
        if self._max_neighbours_per_packet_cache is not None:
            return self._max_neighbours_per_packet_cache
        self._max_neighbours_per_packet_cache = _get_max_neighbours_per_packet()
        return self._max_neighbours_per_packet_cache

    async def listen(self, loop: asyncio.AbstractEventLoop) -> Tuple[
            asyncio.BaseTransport, asyncio.BaseProtocol]:
        return await loop.create_datagram_endpoint(
            lambda: self, local_addr=(self.address.ip, self.address.udp_port))

    def connection_made(self, transport):
        self.transport = transport

    async def bootstrap(self):
        while self.transport is None:
            # FIXME: Instead of sleeping here to wait until connection_made() is called to set
            # .transport we should instead only call it after we know it's been set.
            await asyncio.sleep(1)
        self.logger.debug("boostrapping with {}".format(self.bootstrap_nodes))
        await self.kademlia.bootstrap(self.bootstrap_nodes)
        self.mydb.dump()

    # FIXME: Enable type checking here once we have a mypy version that
    # includes the fix for https://github.com/python/typeshed/pull/1740
    def datagram_received(self, data: AnyStr, addr: Tuple[str, int]) -> None:  # type: ignore
        ip_address, udp_port = addr
        self.receive(kademlia.Address(ip_address, udp_port), data)  # type: ignore

    def error_received(self, exc: Exception) -> None:
        self.logger.error('error received: {}'.format(exc))

    def send(self, node: kademlia.Node, message: bytes) -> None:
        self.transport.sendto(message, (node.address.ip, node.address.udp_port))

    def stop(self):
        self.logger.info('stopping discovery')
        self.transport.close()

    def receive(self, address: kademlia.Address, message: AnyStr) -> None:
        try:
            remote_pubkey, cmd_id, payload, message_hash = _unpack(message)
        except DefectiveMessage as e:
            self.logger.error('error unpacking message: {}'.format(e))
            return

        # As of discovery version 4, expiration is the last element for all packets, so
        # we can validate that here, but if it changes we may have to do so on the
        # handler methods.
        expiration = rlp.sedes.big_endian_int.deserialize(payload[-1])
        if time.time() > expiration:
            self.logger.error('received message already expired')
            return

        cmd = CMD_ID_MAP[cmd_id]
        if len(payload) != cmd.elem_count:
            self.logger.error('invalid {} payload: {}'.format(cmd.name, payload))
            return
        node = kademlia.Node(remote_pubkey, address)
        handler = self._get_handler(cmd)
        handler(node, payload, message_hash)

    def recv_pong(self, node: kademlia.Node, payload: List[Any], _: AnyStr) -> None:
        # The pong payload should have 3 elements: to, token, expiration
        _, token, _ = payload
        self.kademlia.recv_pong(node, token)

    def recv_neighbours(self, node: kademlia.Node, payload: List[Any], _: AnyStr) -> None:
        # The neighbours payload should have 2 elements: nodes, expiration
        nodes, _ = payload
        
        self.mydb.add_response(node, _extract_nodes_from_payload(nodes))
        try:
            pass
        except Exception as e:
            print("Error in adding resposne: " + str(e))
            logging.error(e)

        self.kademlia.recv_neighbours(node, _extract_nodes_from_payload(nodes))

    def recv_ping(self, node: kademlia.Node, _, message_hash: AnyStr) -> None:
        self.kademlia.recv_ping(node, message_hash)

    def recv_find_node(self, node: kademlia.Node, payload: List[Any], _: AnyStr) -> None:
        # The find_node payload should have 2 elements: node_id, expiration
        self.logger.debug('<<< find_node from {}'.format(node))
        node_id, _ = payload
        self.kademlia.recv_find_node(node, big_endian_to_int(node_id))

    def send_ping(self, node: kademlia.Node) -> bytes:
        self.logger.debug('>>> pinging {}'.format(node))
        version = rlp.sedes.big_endian_int.serialize(PROTO_VERSION)
        payload = [version, self.address.to_endpoint(), node.address.to_endpoint()]
        message = _pack(CMD_PING.id, payload, self.privkey)
        self.send(node, message)
        # Return the msg hash, which is used as a token to identify pongs.
        return message[:MAC_SIZE]

    def send_find_node(self, node: kademlia.Node, target_node_id: int) -> None:
        target_node_id = int_to_big_endian(
            target_node_id).rjust(kademlia.k_pubkey_size // 8, b'\0')
        self.logger.debug('>>> find_node to {}'.format(node))
        message = _pack(CMD_FIND_NODE.id, [target_node_id], self.privkey)
        self.send(node, message)

    def send_pong(self, node: kademlia.Node, token: AnyStr) -> None:
        self.logger.debug('>>> ponging {}'.format(node))
        payload = [node.address.to_endpoint(), token]
        message = _pack(CMD_PONG.id, payload, self.privkey)
        self.send(node, message)

    def send_neighbours(self, node: kademlia.Node, neighbours: List[kademlia.Node]) -> None:
        nodes = []
        neighbours = sorted(neighbours)
        for n in neighbours:
            nodes.append(n.address.to_endpoint() + [n.pubkey.to_bytes()])

        max_neighbours = self._get_max_neighbours_per_packet()
        for i in range(0, len(nodes), max_neighbours):
            message = _pack(CMD_NEIGHBOURS.id, [nodes[i:i + max_neighbours]], self.privkey)
            self.logger.debug('>>> neighbours to {}: {}'.format(
                node, neighbours[i:i + max_neighbours]))
            self.send(node, message)


@to_list
def _extract_nodes_from_payload(
        payload: List[Tuple[str, str, str, str]]) -> Generator[kademlia.Node, None, None]:
    for item in payload:
        ip, udp_port, tcp_port, node_id = item
        address = kademlia.Address.from_endpoint(ip, udp_port, tcp_port)
        yield kademlia.Node(keys.PublicKey(node_id), address)


def _get_max_neighbours_per_packet():
    # As defined in https://github.com/ethereum/devp2p/blob/master/rlpx.md, the max size of a
    # datagram must be 1280 bytes, so when sending neighbours packets we must include up to
    # _max_neighbours_per_packet and if there's more than that split them across multiple
    # packets.
    # Use an IPv6 address here as we're interested in the size of the biggest possible node
    # representation.
    addr = kademlia.Address('::1', 30303, 30303)
    node_data = addr.to_endpoint() + [b'\x00' * (kademlia.k_pubkey_size // 8)]
    neighbours = [node_data]
    expiration = rlp.sedes.big_endian_int.serialize(int(time.time() + EXPIRATION))
    payload = rlp.encode([neighbours] + [expiration])
    while HEAD_SIZE + len(payload) <= 1280:
        neighbours.append(node_data)
        payload = rlp.encode([neighbours] + [expiration])
    return len(neighbours) - 1


def _pack(cmd_id: int, payload: List[Any], privkey: datatypes.PrivateKey) -> bytes:
    """Create and sign a UDP message to be sent to a remote node.

    See https://github.com/ethereum/devp2p/blob/master/rlpx.md#node-discovery for information on
    how UDP packets are structured.
    """
    cmd_id = force_bytes(chr(cmd_id))
    expiration = rlp.sedes.big_endian_int.serialize(int(time.time() + EXPIRATION))
    encoded_data = cmd_id + rlp.encode(payload + [expiration])
    signature = privkey.sign_msg(encoded_data)
    message_hash = keccak(signature.to_bytes() + encoded_data)
    return message_hash + signature.to_bytes() + encoded_data


def _unpack(message: AnyStr) -> Tuple[datatypes.PublicKey, int, List[Any], AnyStr]:
    """Unpack a UDP message received from a remote node.

    Returns the public key used to sign the message, the cmd ID, payload and hash.
    """
    message_hash = message[:MAC_SIZE]
    if message_hash != keccak(message[MAC_SIZE:]):
        raise WrongMAC()
    signature = keys.Signature(message[MAC_SIZE:HEAD_SIZE])
    signed_data = message[HEAD_SIZE:]
    remote_pubkey = signature.recover_public_key_from_msg(signed_data)
    cmd_id = safe_ord(message[HEAD_SIZE])
    cmd = CMD_ID_MAP[cmd_id]
    payload = rlp.decode(message[HEAD_SIZE + 1:], strict=False)
    # Ignore excessive list elements as required by EIP-8.
    payload = payload[:cmd.elem_count]
    return remote_pubkey, cmd_id, payload, message_hash


if __name__ == "__main__":
    async def show_tasks():
        while True:
            tasks = []
            for task in asyncio.Task.all_tasks():
                if task._coro.__name__ != "show_tasks":
                    tasks.append(task._coro.__name__)
            if tasks:
                logger.debug("Active tasks: {}".format(tasks))
            await asyncio.sleep(3)

    privkey_hex = '65462b0520ef7d3df61b9992ed3bea0c56ead753be7c8b3614e0ce01e4cac41b'
    listen_host = '0.0.0.0'
    listen_port = 30303
    bootstrap_uris = bootstrap.bootstrap_uris

    logger = logging.getLogger("evm.p2p.discovery")
    #logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s', filename="discoverylog.log")
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    privkey = keys.PrivateKey(decode_hex(privkey_hex))
    addr = kademlia.Address(listen_host, listen_port, listen_port)
    bootstrap_nodes = [kademlia.Node.from_uri(x) for x in bootstrap_uris]
    discovery = DiscoveryProtocol(privkey, addr, bootstrap_nodes)
    loop.run_until_complete(discovery.listen(loop))

    # There's no need to wait for bootstrap because we run_forever().
    asyncio.ensure_future(discovery.bootstrap())

    # This helps when debugging asyncio issues.
    # task_monitor = asyncio.ensure_future(show_tasks())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print(discovery.mydb)
        pass

    # task_monitor.set_result(None)
    discovery.stop()
    # logger.info("Pending tasks at exit: {}".format(asyncio.Task.all_tasks(loop)))
    loop.close()
