import unittest

from lab_1 import test_gen_file
from lab_1.binary_tree_class import generate_binary_tree, print_binary_tree

if __name__ == '__main__':
    unittest.main(module=test_gen_file, exit=False)
    tree = generate_binary_tree(height=10, root=14)
    print_binary_tree(tree)
