import btree
import logging
#import mylogger

#mylogger.config_logs()
logging.getLogger().setLevel(logging.DEBUG)

myTree = btree.Tree(5)

myTree.add(1)
myTree.add(2)
myTree.add(3)
myTree.add(4)
myTree.add(5)
myTree.add(32)
#myTree.printTree()
print(myTree)

print(myTree.closest_stump().get_stump_path())
