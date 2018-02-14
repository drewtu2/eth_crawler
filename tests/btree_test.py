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

if __name__ == '__main__':
    unittest.main()
