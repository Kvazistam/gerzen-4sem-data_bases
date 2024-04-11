import unittest
from binary_tree_class import *

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root =14
        self.height = 5
        self.binary_tree = generate_binary_tree(self.root,self.height)

    def test_root_value(self):
        self.assertEqual(self.binary_tree[0], self.root)

    def test_number_of_nodes(self):
        def count_nodes(tree):
            if not tree:
                return 0
            return 1 + sum(count_nodes(child) for child in tree[1])

        self.assertEqual(count_nodes(self.binary_tree), 2**(self.height)-1)

    def test_tree_structure(self):
        def is_binary_tree(tree):
            if not tree:
                return True
            if len(tree) != 2 or not isinstance(tree[1], list):
                return False
            for child in tree[1]:
                if not is_binary_tree(child):
                    return False
            return True

        self.assertTrue(is_binary_tree(self.binary_tree))

if __name__ == '__main__':
    unittest.main()