# Write a function, depth_first_values, that takes in the root of 
# a binary tree. The function should return a list containing all 
# values of the tree in depth-first order.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"{self.val}"


# Iterative approach. Uses a stack to accumulate the values to be processed.
# Note that we append and pop values. So the important part is the order in which
# we do so to favor the left side of the tree.
#
# Time complexity: O(n)
# Space complexity: O(n)

def depth_first_values(root):
    if root is None:
        return []
    values = []
    stack = [root]
    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return values

# Recursive approach

def depth_first_values_recursive(root):
    if root is None:
        return []
    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)
    return [root.val, *left_values, *right_values]

def test_depth_first_values():
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

    res = depth_first_values(a)
    expected = ['a', 'b', 'd', 'e', 'c', 'f']
    assert res == expected

    res2 = depth_first_values_recursive(a)
    assert res2 == expected