import random
from tree import BinarySearchTree

random.seed(77)

def random_tree(size=42):
    values = random.sample(range(1, 1000), 42)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def example_tree():
    values = [45, 20, 30, 60, 81, 97, 100, 7, 8, 4]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def extended_tree():
    values = [45, 20, 30, 60, 81, 97, 100, 8, 4]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

bst = extended_tree()
bst.inorder_traversal()

# testar remoção da árvore
print('\n----')
v = 7
bst.remove(v)
print("Após remover {}".format(v))
bst.levelorder_traversal()
