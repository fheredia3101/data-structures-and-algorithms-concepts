# Write a function, linked_list_find, that
# takes in the head of a linked list and a
# target value. The function should return
# a boolean indicating whether or not the
# linked list contains the target.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
# Time complexity: O(n)
# Space complexity: O(1)

def linked_list_find(head, target):
    if target is None:
        return False
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False

# Recursive
# Time complexity: O(n)
# Space complexity: O(n)

def linked_list_find_recursive(head, target):
    # base case
    if target is None:
        return False
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find_recursive(head.next, target)

def test_linked_list():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    assert linked_list_find(a, "c") is True
    assert linked_list_find(a, "d") is True
    assert linked_list_find(a, "q") is False
    assert linked_list_find(a, None) is False
    assert linked_list_find(None, "a") is False

    assert linked_list_find_recursive(a, "c") is True
    assert linked_list_find_recursive(a, "d") is True
    assert linked_list_find_recursive(a, "q") is False
    assert linked_list_find_recursive(a, None) is False
    assert linked_list_find_recursive(None, "a") is False