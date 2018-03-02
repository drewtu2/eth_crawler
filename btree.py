import logging
from collections import deque

        

class Tree:
    """
    The Tree structure.
    """
    LEFT = 0
    RIGHT = 1
    
    def __init__(self, bit_length = 8):
        self.NUM_BITS = bit_length 
        self.root = None
    def __str__(self):
        return self.root.__str__()
    
    def getRoot(self):
        return self.root

    def add(self, val):
        """
        Takes a given value and inserts it into the correct leaf at the bottom
        of the tree. Constructs the branches going down to that tree in the process. 
        Depth is determined by self.NUM_BITS
        """

        def _add(node: Node, depth = self.NUM_BITS) -> Node:
            """
            Determines which direciton the node value should be added
            """

            if(node.prefix is None):
                logging.debug("node none at depth: {}".format(depth))

            # This node is the last node
            if depth == 0:
                child_node = Node(val)
                child_node.end = True
                node.l = child_node 
            # Node goes left
            elif utils.nth_bit(val, depth) == self.LEFT:
                node = _add_direction(node, depth, self.LEFT)
            # Node goes right
            else:
                node = _add_direction(node, depth, self.RIGHT)
            
            return node
        
        def _add_direction(node, depth, direction):
            """
            Adds the value as a child node in the given direction
            """
            logging.debug("{} at bit {} is {}".format(val, depth, direction))
            
            if direction == self.LEFT:
                targeted_child = node.l
            else:
                targeted_child = node.r

            if targeted_child is None:
                targeted_child = Node(direction)
            targeted_child.prefix = list(node.prefix)
            targeted_child.prefix.append(direction)
            
            # TODO// REFACTOR this
            if direction == self.LEFT:
                node.l = _add(targeted_child, depth - 1)
            else:
                node.r = _add(targeted_child, depth - 1)

            return node
        
        # Actual fx
       
        assert(val < 2**self.NUM_BITS)
        
        if(self.root == None):
            self.root = Node('R')
        self.root = _add(self.root)
    
    def add_list(self, list_of_nodes):
        for node in list_of_nodes:
            self.add(node)

    def find(self, val):
        if(self.root is not None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l is not None):
            self._find(val, node.l)
        elif(val > node.v and node.r is not None):
            self._find(val, node.r)
    
    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def highest_stump_node(self):
        """
         BFS on tree to find the highest stump. Stump is defined as a node with
         at least one missing child. ROOT is max height.
        """

        visited, queue = set(), deque([self.root])
        
        while queue:
            vertex = queue.popleft()
            
            if vertex.is_stump():
                break
            
            visited.add(vertex)
            # new nodes are added to end of queue
            queue.extend([vertex.l, vertex.r])
        
        return vertex
    
    def path_to_stump(self) -> int:
        """
        Returns a node id from the given stump.
        If path to stump node is 110 and node 110-001 exists, path_to_stump 
        will integer representation of 110-100 (110-1xx where x will be 0)
        """
        prefix = list(self.highest_stump_node().get_stump_path())
        
        num_bits_needed = self.NUM_BITS - len(prefix)
        
        prefix += [0] * num_bits_needed
        logging.debug("Stump binary: {}".format(prefix))
        # Prefix holds the array representation, convert to integer. 
        stump = int("".join(map(str, prefix)), 2) 
        logging.info("Farthest stump is {}".format(stump))
        return stump

class Node:
    """
    A Node in a binary tree
    """
    def __init__(self, val):
        self.l = None   # Node to the left
        self.r = None   # Node to the right
        self.v = val    # The bit represented by this node a 1 or 0
        self.prefix = [] # The path value to this node. 
                        # ( each index represents a node)
        self.marked = False;
        self.end = False
    
    def is_stump(self):
        """
        Returns true if this node is a stump
        """
        return self.l is None or self.r is None
    
    def get_stump_path(self):
        """
        Returns the path to the node of a stump. 
        """
        temp_prefix = list(self.prefix)
        
        if self.l is None:
            temp_prefix.append(0)
        elif self.r is None:
            temp_prefix.append(1)
        else:
            return None
        return temp_prefix
    
    def __str__(self, level=0):
        """
        String representation
        """
        if self.end:
            ret = "\t"*(level - 1) + "(" + repr(self.v) + ")\n"
        else:
            ret = "\t"*level + repr(self.v) + "\n"
            if self.l is not None:
                ret += self.l.__str__(level+1)
            if self.r is not None:
                ret += self.r.__str__(level+1)
        return ret

class utils():
    """
    Random helpers.
    """
    @staticmethod
    def nth_bit(num: int, bit_number: int) -> int:
        """
        Returns the value of the bit_index'th bit in a given number
        """
        return (num>>(bit_number - 1)) & 1
        
    @staticmethod
    def set_bit(v, index, x):
        """
        Set the index:th bit of v to 1 if x is truthy, else to 0, and 
        return the new value.
        """
        mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
        v &= ~mask          # Clear the bit indicated by the mask (if x is False)
        if x:
            v |= mask         # If x was True, set the bit indicated by the mask.
        return v            # Return the result, we're done.
