# Implementation of a basic linked list traversal
#
# Time complexity: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> None

def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

def print_list_recursive(head):
    if not head:
        return
    print(head.val)
    print_list_recursive(head.next)

def test_print_list():
    print_list(a)
    print_list_recursive(a)