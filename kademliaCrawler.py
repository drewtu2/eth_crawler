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
    NewType,
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

from evm.constants import (
    UINT_256_MAX,
    UINT_256_CEILING,
)

from evm.utils.keccak import keccak
import evm.utils.numeric
from evm.utils.numeric import (big_endian_to_int, int_to_big_endian)

# Workaround for import cycles caused by type annotations:
# http://mypy.readthedocs.io/en/latest/common_issues.html#import-cycles
if TYPE_CHECKING:
    from evm.p2p.discovery import DiscoveryProtocol  # noqa: F401

from evm.p2p import kademlia

# My Stuff for debuggin
import sys
import traceback 
import btree 
from pympler import summary, muppy, asizeof
from pympler.classtracker import ClassTracker

NewType('DistanceResult', Dict[int, Set[kademlia.Node]])

class KademliaCrawlerProtocol(kademlia.KademliaProtocol):
    logger = logging.getLogger("KademliaCrawlerProtocol")

    def __init__(self, node: kademlia.Node, wire: 'DiscoveryProtocol') -> None:
        super(KademliaCrawlerProtocol, self).__init__(node, wire)
        self.logger.debug("Kademlia Crawler Created")

        self.tracker = ClassTracker()
        self.myTree = btree.Tree(256)
        self.tracker.track_object(self.myTree)

        self.MAX_CONCURRENT = 64;

    async def bootstrap(self, bootstrap_nodes: List[kademlia.Node]) -> None:
        bonded = await asyncio.gather(*[self.bond(n) for n in bootstrap_nodes])
        if not any(bonded):
            self.logger.info("Failed to bond with bootstrap nodes {}".format(bootstrap_nodes))
            return
        await self.lookup(self.this_node.id)

    async def lookup(self, node_id: int, use_k_bucket = True) -> List[kademlia.Node]:
        """Lookup performs a network search for nodes close to the given target.

        It approaches the target by querying nodes that are closer to it on each 
        iteration. The given target does not need to be an actual node identifier.
        """
        self.logger.info("Kademlia Crawler Lookup Initiated")
        nodes_asked = set()  # type: Set[Node]
        nodes_seen = set()   # type: Set[Node]

        async def _find_node(node_id, remote, semaphore):
            async with semaphore:
                self.wire.send_find_node(remote, node_id)
                candidates = await self.wait_neighbours(remote)
                
                if len(candidates) == 0:
                    self.logger.debug("got no candidates from {}, returning".format(remote))
                    return candidates

                candidates = [c for c in candidates if c not in nodes_seen]
                self.logger.debug("got {} new candidates".format(len(candidates)))
                # Add new candidates to nodes_seen so that we don't attempt to 
                # bond with failing ones in the future.
                nodes_seen.update(candidates)
                bonded = await asyncio.gather(*[self.bond(c) for c in candidates])
                self.logger.debug("bonded with {} candidates".format(bonded.count(True)))
            
            return [c for c in candidates if bonded[candidates.index(c)]]

        def _exclude_if_asked(nodes):
            nodes_to_ask = list(set(nodes).difference(nodes_asked))
            return kademlia.sort_by_distance(nodes_to_ask, node_id)[:kademlia.k_find_concurrency]

        # Get all of the nodes in our list, not just the closest k_bucket nodes
        closest = self.routing.neighbours(node_id)
        self.logger.debug("starting lookup; initial neighbours: {}".format(closest))
        nodes_to_ask = _exclude_if_asked(closest)
        mySem = asyncio.Semaphore(value = self.MAX_CONCURRENT)
        
        while nodes_to_ask:
            
            #summary.print_(summary.summarize(muppy.get_objects()))
            #print('Tasks count: ', len(asyncio.Task.all_tasks()))
            #print('Active tasks count: ', len(
            #[task for task in asyncio.Task.all_tasks() if not task.done()]))

            self.logger.debug("node lookup; querying {}".format(nodes_to_ask))
            nodes_asked.update(nodes_to_ask)

            tasks = [_find_node(node_id, n, mySem) for n in nodes_to_ask];

            results = await asyncio.gather(*tasks)
            
            for candidates in results:
                closest.extend(candidates)
            
            # Here we're keeping all of the nodes that were returned so that we 
            # can get a better view of the entire network.  
            if use_k_bucket:
                closest = kademlia.sort_by_distance(closest, node_id)[:kademlia.k_bucket_size]
            else:
                closest = kademlia.sort_by_distance(closest, node_id)
            nodes_to_ask = _exclude_if_asked(closest)

        self.logger.info("lookup finished for {}: {} nodes discovered".format(node_id, len(closest)))
        return closest
    
    async def crawl(self):
        """
        Continue to look up random nodes until no new nodes are discovered. 
        """
        def _extract_new_nodes(nodes: List[kademlia.Node]) -> List[kademlia.Node]:
            """
            Returns a list of nodes that we havne't previously encountered
            """
            return [node.id for node in nodes if node.id not in known_nodes]
        
        known_nodes = [] # Will be a list of node ids

        # Populate our known nodes with nodes near us
        new_nodes = await self.lookup(self.this_node.id, False)
        print("Size of new nodes pre strip: " + str(asizeof.asizeof(new_nodes)))
        new_nodes = _extract_new_nodes(new_nodes)   # Reduced to list of node ids
        print("Size of new nodes post strip: " + str(asizeof.asizeof(new_nodes)))
        self.myTree.add_list(new_nodes)
        print("Size of myTree: " + str(asizeof.asizeof(self.myTree)))
        known_nodes += new_nodes

        while new_nodes is not []:

            #summary.print_(summary.summarize(muppy.get_objects()))
            #self.tracker.create_snapshot()
            #self.tracker.stats.print_summary()
            #print("Size of known nodes: " + str(asizeof.asizeof(known_nodes)))
            self.logger.debug("In crawl loop... {} new nodes discovered...".format(len(new_nodes)))
            self.logger.info("{} total nodes discovered...".format(len(known_nodes)))
            dump_new_nodes(known_nodes)
            #summary.print_(summary.summarize(muppy.get_objects()))
            
            try:
                new_nodes = await self.lookup(self.myTree.path_to_stump(), False)
                new_nodes = _extract_new_nodes(new_nodes)
                self.myTree.add_list(new_nodes)
                known_nodes += new_nodes
            except evm.p2p.kademlia.AlreadyWaiting as e:
                self.logger.error(e)
        
        self.logger.info("Crawled newtork... {} nodes found...".format(len(known_nodes)))
        return known_nodes

    async def targeted_crawl(self, remote: kademlia.Node) -> List[kademlia.Node]:

        def print_neighbours_list(low, searched, high):
            def _get_neighbour(result, index):
                if index >= len(result["neighbours"]):
                    return ""
                else:
                    node = list(result["neighbours"])[index]
                    #return str(node) + " (" + str(hex(_xor_distance(node.id, remote.id))) + ")"
                    return str(node) 
        
            result_lengths = [len(x["neighbours"]) for x in [low, searched, high]]
        
            print(header_string("Search Result"))
        
            print("Low" + " " * 29 + "\t Searched " + " " * 29 + "\t High")
            for index in range(0, max(result_lengths) - 1):
                low_n = _get_neighbour(low, index)
                searched_n = _get_neighbour(searched, index)
                high_n = _get_neighbour(high, index)
                
                print(low_n + "\t" + searched_n + "\t" + high_n)
            print()

        async def _find_node_at_distance(distance: int):
            """
            Sends a find_node request to the remote node at a given distance from
            the node we're targeting. Returns all of the nodes given in the response. 
            """
            node_id = _node_at_distance(remote, distance)
            self.logger.debug("Searching for node: %d", node_id)

            self.wire.send_find_node(remote, node_id)
            candidates = await self.wait_neighbours(remote)
            if len(candidates) == 0:
                self.logger.warning("got no candidates from {}, returning".format(remote))

            return candidates
#            candidates = [c for c in candidates if c not in nodes_seen]
#            self.logger.debug("got {} new candidates".format(len(candidates)))
#            # Add new candidates to nodes_seen so that we don't attempt to bond with failing ones
#            # in the future.
#            nodes_seen.update(candidates)
#            bonded = await asyncio.gather(*[self.bond(c) for c in candidates])
#            self.logger.debug("bonded with {} candidates".format(bonded.count(True)))
#            return [c for c in candidates if bonded[candidates.index(c)]]


        #def recurse_step(interest_low, interest_high):
        async def recurse_step(interest_low: 'DistanceResult', interest_high: 'DistanceResult'):
            """
            {
                "distance": int,
                "neighbours": Set([kademlia.Node])
            }
            :d_start: The closest distance to the remote node
            :interest_high: The furthest distance from the remote node
            """
           
            d_interest = int((interest_low["distance"] + interest_high["distance"])//2)

            self.logger.info(
                    "Performing Recursive Search...\n" + 
                    "Max Distance: {}\n".format(hex(interest_high["distance"])) + 
                    "Mid Distance: {}\n".format(hex(d_interest)) + 
                    "Min Distance: {}".format(hex(interest_low["distance"])))
            
            if (interest_high["distance"] == d_interest):
                self.logger.warning("Error... high = mid\n")
                print_neighbours_list(interest_low, interest_high, interest_high)
                _compare_nodes_at_distance(remote, interest_low["distance"], interest_high["distance"])
                return interest_high["neighbours"]
            elif (interest_low["distance"] == d_interest):
                self.logger.warning("Error... low = mid\n")
                print_neighbours_list(interest_low, interest_low, interest_high)
                _compare_nodes_at_distance(remote, interest_low["distance"], interest_high["distance"])
                return interest_low["neighbours"]
            
            interest_result = make_distanceResult(d_interest, 
                    await _find_node_at_distance(d_interest))

            print_neighbours_list(interest_low, interest_result, interest_high)
            disjoint_up = interest_result["neighbours"].isdisjoint(interest_high["neighbours"])
            disjoint_down = interest_result["neighbours"].isdisjoint(interest_low["neighbours"])

            if not disjoint_up and not disjoint_down:
                # This is a BASE CASE
                # We overlap completely with both bounds. return this iteraiton. 
                self.logger.info("Hit base case!\n")
                return interest_result["neighbours"]
            elif disjoint_up and not disjoint_down:
                # Overlapped bottom, but not top: check top 
                # Check [d_interst, interest_high]
                self.logger.info("Overlapped bottom, but not top - Search up!\n")
                interest_result["neighbours"].update(\
                        await recurse_step(interest_result, interest_high))
                return interest_result["neighbours"]
            elif not disjoint_up and disjoint_down:
                # Overlapped top, but not bottom: check bottom 
                # Check [interest_low, interest_result]
                self.logger.info("Overlapped top, but not bottom - Search down!\n")
                
                interest_result["neighbours"].update(\
                        await recurse_step(interest_low, interest_result))
                return interest_result["neighbours"]
            else:
                # Overlapped neither. search both. 
                #recurse_tasks = [
                #        recurse_step(interest_low, interest_result),\
                #        recurse_step(interest_result, interest_high)]
                #responses = await asyncio.gather(*recurse_tasks)
                self.logger.info("No Overalp: search both\n")
                
                responses = await recurse_step(interest_low, interest_result)
                responses.update(await recurse_step(interest_result, interest_high))
                interest_result["neighbours"].update(responses)
                return interest_result["neighbours"]

        furthest_node = make_distanceResult(_max_distance_to_node(), 
                await _find_node_at_distance(_max_distance_to_node()))
        closest_node = make_distanceResult(0, 
                await _find_node_at_distance(0))
        try:
            addr_book = await recurse_step(closest_node, furthest_node)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            traceback.print_tb(exc_tb)
            print(e)
        finally:
            addr_book = set()
        return addr_book


def _node_at_distance(node: kademlia.Node, distance: int) -> int:
    """
    Returns the node id exaclty distance away from a given id. Distance is 
    based on the XOR metric.
    """
    return node.id ^ distance

def _xor_distance(d1: int, d2: int) -> int:
    return d1 ^ d2

def _compare_nodes_at_distance(node: kademlia.Node, distance1: int, distance2: int):
    """
    Prints some information about the nodes at two distances
    """
    def _gen_node_info(distance):
        """
        Returns a dictionary with information about the node at a given distance
        """
        node_info = {
            # The id of the node at a given distance.
            "id": _node_at_distance(node, distance),
            "distance": distance
        }
        return node_info
    
    def _param_2_str(param: str, d1, d2) -> str:
        str1 = param + "1:" + str(hex(d1))
        str2 = param + "2:" + str(hex(d2))
        return str1 + "\n" + str2
    
    node_d1 = _gen_node_info(distance1)
    node_d2 = _gen_node_info(distance2)
    
    print(header_string("Node Comparison")) 
    print(_param_2_str("XOR Distance", node_d1["distance"], node_d2["distance"]))
    print()
    print("Remote Node:", str(hex(node.id)))
    print(_param_2_str("Node Id", node_d1["id"], node_d2["id"]))
    
    print("XOR distance differences:", str(hex(abs(node_d1["distance"] - node_d2["distance"]))))
    print("XOR distance of node ids:", str(hex(_xor_distance(node_d1["id"], node_d2["id"]))))
    print()

def _max_distance_to_node() -> int:
    """
    Returns the maximum possible distance to this_node 
    Distance is based on the XOR metric, therefore, max distance is the 
    inverse of the node id which is equal to a number that is all 1's the 
    size of node id. 
    """
    return UINT_256_MAX

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

def make_distanceResult(distance: int, neighbours: List[kademlia.Node]):
    """
    Returns the distance result of a given distance and neighbour
    """

    result = {\
        "distance": distance,\
        "neighbours": set(neighbours)}
    
    if neighbours == None:
        print("\n" * 3)
        print("Error: result is nonetype")
        print("\n" * 3)

    return result

def header_string(header: str) -> str:
    """
    Takes a string and returns a string with 100 stars wrapping it and the
    given string centered in the middle
    Ex. 
    ***** .... ****
    *  my string  *
    ***** .... ****
    """
    line_len = 100
    stars = 2
    spaces_per_side = " " * ((line_len - stars - len(header)) // 2)
    if len(header) % 2 == 0:
        odd_space = ""
    else:
        odd_space = " "

    return ("*" * line_len + "\n" 
    + "*" + spaces_per_side + header + spaces_per_side + odd_space + "*\n"
    + "*" * line_len + "\n")

def dump_new_nodes(nodes):
    with open("logs/nodes_log.log", "a+") as f:
        f.write("Nodes discovered: {}\n".format(len(nodes)))

