import unittest
import btree

class TestBtree(unittest.TestCase):
    
    def setUp(self):
        self.tree = btree.Tree(3)

    def test_empty(self):
        self.assertEqual(self.tree.__str__(), 'None')

    def test_add_1(self):
        self.tree.add(1)
        one_str = "\'R\'\n" + "\t0\n" + "\t\t0\n" + "\t\t\t1\n" + "\t\t\t(1)\n"
        self.assertEqual(self.tree.__str__(), one_str)
    
    def test_add_5(self):
        self.tree.add(1)
        self.tree.add(5)
        one_str = "\'R\'\n" + "\t0\n" + "\t\t0\n" + "\t\t\t1\n" + "\t\t\t(1)\n"
        five_str = "\t1\n" + "\t\t0\n" + "\t\t\t1\n" + "\t\t\t(5)\n"
        self.assertEqual(self.tree.__str__(), one_str + five_str)
    
    def test_add_list(self):
        self.tree.add_list([1, 5])
        one_str = "\'R\'\n" + "\t0\n" + "\t\t0\n" + "\t\t\t1\n" + "\t\t\t(1)\n"
        five_str = "\t1\n" + "\t\t0\n" + "\t\t\t1\n" + "\t\t\t(5)\n"
        self.assertEqual(self.tree.__str__(), one_str + five_str)
    
    def test_get_stump(self):
        self.tree.add(1)
        stump_value = self.tree.path_to_stump()
        self.assertEqual(4, stump_value) 
        
        # Make sure the BFS next stump is found
        self.tree.add(stump_value)
        stump_value = self.tree.path_to_stump()
        self.assertEqual(2, stump_value)

if __name__ == '__main__':
    unittest.main()
