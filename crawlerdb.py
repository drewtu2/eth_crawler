from evm.p2p import kademlia
import logging
from typing import (
        Any,
        AnyStr,
        Callable,
        Generator,
        List,
        Tuple
)
import pickle 

class CrawlerDb():

    def __init__(self):
        """
        {
        node1: [node2, node3, ...., noden],
        node2: [ndod1, node3, ...., noden],
        ...
        }
        """
        self.node_neighbors = {}
    def __str__(self):
        this_string = ""
        for key in self.node_neighbors:
            this_string += (str(key) + ": \n") 
            this_string += ("Num neighbors: " + str(len(self.node_neighbors[key])))
            this_string += "\n"
            for entry in self.node_neighbors[key]:
                this_string +=  "\t" + str(entry) + "\n"
        
        this_string += "Total neighbors: " + str(len(self.node_neighbors))
        return this_string

    def add_response(self, node: kademlia.Node, payload: List[Any]):
        """
        Takes a response and extracts all the new nodes for the list. Add the
        new nodes to the node neighbor list. 
        
        """
        def _exclude_if_exists(nodes: List[Any]):
            """
            Return a list of nodes that havnen't been discovered before
            """
            if str(node) in self.node_neighbors:
                current_known = self.node_neighbors[str(node)]
            else:
                current_known = []
            
            new_nodes = [node for node in nodes if node not in current_known]
            return new_nodes
        
        # Process the response and add it to the correct place 
        try:
            if str(node) in self.node_neighbors:
                logging.debug("%s already exists....", str(node))
                self.node_neighbors[str(node)] += _exclude_if_exists(payload)
            else:
                logging.debug("%s doesn't exist. creating...", str(node))
                self.node_neighbors[str(node)] = _exclude_if_exists(payload)
        except KeyError as e:
            logging.error(e)
            #print("Error adding " + str(node) + " details...")
    def dump(self, dumpFile="neighbors.pickle"):
        with open(dumpFile, "w") as fp:
            pickle.dump(self.node_neighbors, fp)
        logging.info("Wrote neighbors to file")
