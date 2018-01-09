import asyncio
import ipaddress
import logging
import bisect
import operator
import random
import struct
import time
import urllib
from functools import total_ordering
from typing import (  # noqa: F401
    AnyStr,
    Callable,
    Dict,
    List,
    Set,
    Sized,
    Tuple,
    TYPE_CHECKING,
)

from eth_utils import (
    decode_hex,
    encode_hex,
    force_bytes,
)

from eth_keys import (
    datatypes,
    keys,
)

from evm.utils.keccak import keccak
from evm.utils.numeric import (big_endian_to_int, int_to_big_endian)


# Workaround for import cycles caused by type annotations:
# http://mypy.readthedocs.io/en/latest/common_issues.html#import-cycles
if TYPE_CHECKING:
    from evm.p2p.discovery import DiscoveryProtocol  # noqa: F401

from evm.p2p import kademlia

class KademliaCrawlerProtocol(kademlia.KademliaProtocol):
    logger = logging.getLogger("KademliaCrawlerProtocol")

    def __init__(self, node: kademlia.Node, wire: 'DiscoveryProtocol') -> None:
        super(KademliaCrawlerProtocol, self).__init__(node, wire)
        self.logger.debug("Kademlia Crawler Created")

    async def bootstrap(self, bootstrap_nodes: List[kademlia.Node]) -> None:
        bonded = await asyncio.gather(*[self.bond(n) for n in bootstrap_nodes])
        if not any(bonded):
            self.logger.info("Failed to bond with bootstrap nodes {}".format(bootstrap_nodes))
            return
        await self.lookup(self.this_node.id)

    async def lookup(self, node_id: int, use_k_bucket = True) -> List[kademlia.Node]:
        """Lookup performs a network search for nodes close to the given target.

        It approaches the target by querying nodes that are closer to it on each iteration.  The
        given target does not need to be an actual node identifier.
        """
        self.logger.debug("Kademlia Crawler Lookup Initiated")
        nodes_asked = set()  # type: Set[Node]
        nodes_seen = set()   # type: Set[Node]

        async def _find_node(node_id, remote):
            self.wire.send_find_node(remote, node_id)
            candidates = await self.wait_neighbours(remote)
            if len(candidates) == 0:
                self.logger.debug("got no candidates from {}, returning".format(remote))
                return candidates
            candidates = [c for c in candidates if c not in nodes_seen]
            self.logger.debug("got {} new candidates".format(len(candidates)))
            # Add new candidates to nodes_seen so that we don't attempt to bond with failing ones
            # in the future.
            nodes_seen.update(candidates)
            bonded = await asyncio.gather(*[self.bond(c) for c in candidates])
            self.logger.debug("bonded with {} candidates".format(bonded.count(True)))
            return [c for c in candidates if bonded[candidates.index(c)]]

        def _exclude_if_asked(nodes):
            nodes_to_ask = list(set(nodes).difference(nodes_asked))
            return kademlia.sort_by_distance(nodes_to_ask, node_id)[:kademlia.k_find_concurrency]

        # Get all of the nodes in our list, not just the closest k_bucket nodes
        closest = self.routing.neighbours(node_id, None)
        self.logger.debug("starting lookup; initial neighbours: {}".format(closest))
        nodes_to_ask = _exclude_if_asked(closest)
        while nodes_to_ask:
            self.logger.debug("node lookup; querying {}".format(nodes_to_ask))
            nodes_asked.update(nodes_to_ask)
            results = await asyncio.gather(
                *[_find_node(node_id, n) for n in nodes_to_ask])
            for candidates in results:
                closest.extend(candidates)
            
            # Here we're keeping all of the nodes that were returned so that we 
            # can get a better view of the entire network.  
            if use_k_bucket:
                closest = kademlia.sort_by_distance(closest, node_id)[:kademlia.k_bucket_size]
            else:
                closest = kademlia.sort_by_distance(closest, node_id)
            nodes_to_ask = _exclude_if_asked(closest)

        self.logger.info("lookup finished for {}: {}".format(node_id, closest))
        return closest
    
    async def crawl(self):
        """
        Continue to look up random nodes until no new nodes are discovered. 
        """
        known_nodes = []
        
        def _extract_new_nodes(nodes: List[kademlia.Node]) -> List[kademlia.Node]:
            """
            Returns a list of nodes that we havne't previously encountered
            """
            return [node for node in nodes if node not in known_nodes]
        
        # Populate our known nodes with nodes near us
        new_nodes = await self.lookup(self.this_node.id, False)
        new_nodes = _extract_new_nodes(new_nodes)
        known_nodes += new_nodes

        while new_nodes is not []:
            self.logger.debug("In crawl loop... {} new nodes discovered...".format(len(new_nodes)))
            self.logger.info("{} total nodes discovered...".format(len(known_nodes)))
            try:
                new_nodes = await self.lookup(random_node().id, False)
                new_nodes = _extract_new_nodes(new_nodes)
                known_nodes += new_nodes
            except evm.p2p.kademlia.AlreadyWaiting as e:
                self.logger.error(e)
        
        self.logger.info("Crawled newtork... {} nodes found...".format(len(known_nodes)))
        return known_nodes
    
    def node_exists(self):
        """
        Returns when every node in the network knows about a given node_id
        """
        pass
            


def random_pubkey():
    """
    Generate a random public key. 
    """
    pk = int_to_big_endian(random.getrandbits(kademlia.k_pubkey_size))
    return keys.PublicKey(b'\x00' * (kademlia.k_pubkey_size // 8 - len(pk)) + pk)


def random_node(nodeid=None):
    """
    Generate a random node. 
    We use the local address for this because we don't care about the ip, 
    only the node_id. 
    """
    address = kademlia.Address('127.0.0.1', 30303)
    node = kademlia.Node(random_pubkey(), address)
    if nodeid is not None:
        node.id = nodeid
    return node

