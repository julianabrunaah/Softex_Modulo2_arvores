import random
from tree import BinarySearchTree

random.seed(100)

def random_tree(size=42):
    values = random.sample(range(1, 1000), 42)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def example_tree():
    values = [15, 6, 18, 3, 7, 16, 20, 4]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def extended_tree():
    values = [15, 6, 18, 3, 7, 16, 20, 4]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

bst = extended_tree()
bst.inorder_traversal()

# testar inserção de valor na árvore
v = int(input('\nDigite um valor: '))
print('\n----')

bst.insert(v)
print("Após inserir o valor {}".format(v))
bst.levelorder_traversal()