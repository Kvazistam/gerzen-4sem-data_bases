# left_leaf = 2-(root-1), right_leaf = root*2
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def generate_binary_tree(root, height):
    root = BinaryTree(root)
    tree_list = []
    tree = (root.value, tree_list)
    stack = [(root, 1, tree_list)]  # Стек для отслеживания текущего уровня и соответствующего узла

    while stack:
        node, level, node_tree = stack.pop()
        if level < height:
            left_value = 2 - (node.value - 1)
            right_value = node.value * 2

            node.left = BinaryTree(left_value)
            node.right = BinaryTree(right_value)
            l_child, r_child = ([], [])
            node_tree.append((left_value, l_child))
            node_tree.append((right_value, r_child))

            stack.append((node.left, level + 1, l_child))
            stack.append((node.right, level + 1, r_child))
    return tree



def print_binary_tree(tree, level=0, prefix='Root: '):
    if tree:
        print(' ' * level * 4 + prefix + str(tree[0]))
        for child in tree[1]:
            print_binary_tree(child, level + 1, prefix='Child: ')


def gen_rec_bin_tree(height: int, root: int):
    tree = {str(root): []}

    # в случае отрицательного значения height или получения в качестве арументов значений для height и root не целых чисел,
    # поднимаем исключение ValueError() с текстом root and/or height values invalid
    left_func = lambda root: root + 3
    right_func = lambda root: root * 2

    if height == 0:
        return tree
    else:
        l_r = left_func(root)
        r_r = right_func(root)
        print(l_r, r_r)
        a = gen_rec_bin_tree(root=l_r, height=height - 1)
        tree[str(root)].append(a)
        b = gen_rec_bin_tree(root=r_r, height=height - 1)
        tree[str(root)].append(b)
    return tree