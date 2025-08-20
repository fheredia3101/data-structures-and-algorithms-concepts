# A binary tree is a tree where each node has at most two chidlren.
# A tree is made of nodes and edges.
# A tree has a root; a node with not parent.
# A tree has leaves, nodes without children.
# 'Classic' binary trees have a single root.
# A 'classic' binary tree has EXACTLY ONE path between the root and any node.
# A tree with no nodes is an empty tree, and it is still considered a binary tree.

# Here is an example node for a typical binary tree class

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

#       a
#      / \
#     b   c
#    / \   \
#   d   e   f

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f