# Write a function, get_node_value, that takes in the head
# of a linked list and an index. The function should return
# the value of the linked list at the specified index.
# 
# If there is no node at the given index, then return None.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
# Time complexity: O(n)
# Space complexity: O(1)

def get_node_value(head, index):
    if index is None:
        return None
    current = head
    count = 0
    while current is not None:
        if count == index:
            return current.val
        current = current.next
        count += 1
    return None

# Recursive
# Time complexity: O(n)
# Space complexity: O(n)

def _get_node_value_helper(head, index, count):
    if head is None:
        return None
    if index == count:
        return head.val
    return _get_node_value_helper(head.next, index, count + 1)

def get_node_value_recursive(head, index):
    if index is None:
        return None
    count = 0
    return _get_node_value_helper(head, index, count)


# Recursive (suggested approach)
# Instead of keeping track of a count variable,
# we decrement the index upon each recursion.
# Whenever we reach an index of 0, it means that
# we have reached the node that we want the value of.
# Doing it in this way, it removes the need for a helper
# function.
#
# Time complexity: O(n)
# Space complexity: O(n)

def get_node_value_recursive_suggested(head, index):
    if index is None:
        return None
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value_recursive_suggested(head.next, index - 1)

# Tests

def test_get_node_value():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    assert get_node_value(a, 2) == 'c'
    assert get_node_value(a, 3) == 'd'
    assert get_node_value(a, 7) == None
    assert get_node_value(a, None) == None
    assert get_node_value(None,2) == None

    assert get_node_value_recursive(a, 2) == 'c'
    assert get_node_value_recursive(a, 3) == 'd'
    assert get_node_value_recursive(a, 7) == None
    assert get_node_value_recursive(a, None) == None
    assert get_node_value_recursive(None,2) == None

    assert get_node_value_recursive_suggested(a, 2) == 'c'
    assert get_node_value_recursive_suggested(a, 3) == 'd'
    assert get_node_value_recursive_suggested(a, 7) == None
    assert get_node_value_recursive_suggested(a, None) == None
    assert get_node_value_recursive_suggested(None,2) == None