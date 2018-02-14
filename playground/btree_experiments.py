import btree
import logging
#import mylogger

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)

myTree = btree.Tree(8)

myTree.add(1)
myTree.add(2)
myTree.add(3)
myTree.add(4)
myTree.add(5)
myTree.add(32)

print(myTree.path_to_stump())
myTree.add(myTree.path_to_stump())
print(myTree.path_to_stump())
myTree.add(myTree.path_to_stump())
print(myTree.path_to_stump())
myTree.add(myTree.path_to_stump())
print(myTree)

#print(myTree.highest_stump_node().get_stump_path())
print(myTree.path_to_stump())
