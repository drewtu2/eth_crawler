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

from evm.utils.keccak import keccak
from evm.utils.numeric import (
    big_endian_to_int,
    int_to_big_endian,
    safe_ord,
)

# The original discovery protocol and kademlia protocol
from evm.p2p import discovery
from evm.p2p import kademlia

# Our modified version of kademlia protocol
import kademliaCrawler
import crawlerdb
import btree

# Moved to boostrap nodes to a different file to keep this cleaner
import bootstrap

import mylogger

class Crawler(discovery.DiscoveryProtocol):
    """A Kademlia-like protocol to discover RLPx nodes."""
    logger = logging.getLogger("CrawlerProto")
    transport = None  # type: asyncio.DatagramTransport
    _max_neighbours_per_packet_cache = None

    def __init__(self, privkey: datatypes.PrivateKey, address: kademlia.Address,
                 bootstrap_nodes: List[kademlia.Node]) -> None:
        super(Crawler, self).__init__(privkey, address, bootstrap_nodes)
        
        # This is my stuff now
        #self.crawler = kademliaCrawler.KademliaCrawlerProtocol(self.this_node, wire=self)
        self.kademlia= kademliaCrawler.KademliaCrawlerProtocol(self.this_node, wire=self)
        self.mydb = crawlerdb.CrawlerDb()

    async def bootstrap(self):
        while self.transport is None:
            # FIXME: Instead of sleeping here to wait until connection_made() is called to set
            # .transport we should instead only call it after we know it's been set.
            self.logger.debug("Waiting...")
            await asyncio.sleep(1)
        self.logger.debug("boostrapping with {}".format(self.bootstrap_nodes))
        await self.kademlia.bootstrap(self.bootstrap_nodes)
        self.logger.info("Completed boostrap")
        #self.mydb.dump()

    def recv_neighbours(self, node: kademlia.Node, payload: List[Any], _: AnyStr) -> None:
        # The neighbours payload should have 2 elements: nodes, expiration
        nodes, _ = payload
        
        try:
            self.mydb.add_response(node, discovery._extract_nodes_from_payload(nodes))
        except Exception as e:
            self.logger.error("Error in adding resposne: " + str(e))
            self.logger.error(e)

        self.kademlia.recv_neighbours(node, discovery._extract_nodes_from_payload(nodes))
    
    async def crawl(self):
        logger.debug("Started Crawl")
        await self.kademlia.crawl()
    
    async def targeted_crawl(self):
        logger.info("Started Targted Crawl")
        random_node = kademliaCrawler.random_node()

        # We can only ask someone we're bonded to. 
        node = self.kademlia.routing.neighbours(random_node.id)[0]

        await self.kademlia.targeted_crawl(node)
    
def crawl_complete(future):
    logger = logging.getLogger("CrawlerProto")

    if future.exception():
        logger.error("Error in future...")
        logger.error(future.exception())
    else:
        logger.info(future.result())

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

    #mylogger.config_logs()
    logger = logging.getLogger("crawler")
    #logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s', filename="discoverylog.log")
    logging.basicConfig(level=logging.INFO , format='%(levelname)s: %(message)s')

    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    privkey = keys.PrivateKey(decode_hex(privkey_hex))
    addr = kademlia.Address(listen_host, listen_port, listen_port)
    bootstrap_nodes = [kademlia.Node.from_uri(x) for x in bootstrap_uris]
    crawler = Crawler(privkey, addr, bootstrap_nodes)
    loop.run_until_complete(crawler.listen(loop))

    # We need to make sure we sucesfully bootsrap before crawling. 
    loop.run_until_complete(crawler.bootstrap())

    # There's no need to wait for crawl because we run_forever().
    mytask = asyncio.ensure_future(crawler.crawl())
    #mytask = asyncio.ensure_future(crawler.targeted_crawl())
    
    mytask.add_done_callback(crawl_complete)

    # This helps when debugging asyncio issues.
    # task_monitor = asyncio.ensure_future(show_tasks())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        # Avoid Error for destroying pending task
        if not mytask.done():
            mytask.cancel()
        print(crawler.mydb)
        pass

    #task_monitor.set_result(None)
    crawler.stop()
    logger.info("Pending tasks at exit: {}".format(asyncio.Task.all_tasks(loop)))
    loop.close()
