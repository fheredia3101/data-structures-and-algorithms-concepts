# Write a function, sum_list, that takes in the head
# of a linked list containing numbers as an argument.
# The function should return the total sum of all
# values in the linked list.
#
# This one is a straightforward accumulation of all
# the elements in the list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative approach
#
# Time complexity: O(n)
# Space complexity: O(1)

def sum_list(head):
    sum = 0
    current = head
    while current is not None:
        sum += current.val
        current = current.next
    return sum

# Recursive approach
#
# Time complexity: O(n)
# Space complexity: O(n) -> due to the call stack

def sum_list_recursive(head):
    if head is None:
        return 0
    return head.val + sum_list_recursive(head.next)


def test_sum_list_1():
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    # 2 -> 8 -> 3 -> -1 -> 7
    assert sum_list(a) == 19
    assert sum_list_recursive(a) == 19

def test_sum_list_2():
    x = Node(38)
    y = Node(4)
    x.next = y

    # 38 -> 4
    assert sum_list(x) == 42
    assert sum_list_recursive(x) == 42

def test_sum_list_3():
    z = Node(100)
    # 100
    assert sum_list(z) == 100
    assert sum_list_recursive(z) == 100