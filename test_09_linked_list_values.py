# Write a function, linked_list_values, 
# that takes in the head of a linked list as
# an argument. The function should return a
# list containing all values of the nodes in
# the linked list.
#
# We'll use an iterative approach.
#
# Time complexity: O(n)
# Space complexity: O(n)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_values(head):
    if head is None:
        return []
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

def test_linked_list_values_1():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    # a -> b -> c -> d
    assert linked_list_values(a) == ['a','b','c','d']

def test_linked_list_values_2():
    x = Node("x")
    y = Node("y")
    x.next = y
    # x -> y
    assert linked_list_values(x) == ['x','y']

def test_linked_list_values_3():
    q = Node("q")
    # q
    assert linked_list_values(q) == ['q']

def test_linked_list_values_4():
    assert linked_list_values(None) == []