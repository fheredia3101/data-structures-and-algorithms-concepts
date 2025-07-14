# Write a function, reverse_list, that takes in the
# head of a linked list as an argument. The function
# should reverse the order of the nodes in the linked
# list in-place and return the new head of the reversed
# linked list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
# At the time of reversal, we will be modifying the
# pointers of each node; We will use a few variables
# to keep track of the order of the nodes in the
# linked list.
#
# Time complexity: O(n)
# Space complexity: O(1)
def reverse_list(head):
    # List empty
    if head is None:
        return None
    if head.next is None:
        return head
    # Linked list is populated and has more than one node.
    prev = None
    current = head
    next = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# Recursive
#
# The code is very similar, but adding the recursive element
# Note that a new argument 'prev' is added, which defaults to
# None.
#
# We still need to save the _next_ node in the list before
# we re-route the pointers.
#
# Time complexity: O(n)
# Space complexity: O(n)

def reverse_list_recursive(head, prev = None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list_recursive(next, head)


def test_reverse_list_1():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # a -> b -> c -> d -> e -> f
    res = reverse_list(a)
    assert res == f
    assert f.next == e
    assert e.next == d
    assert d.next == c
    assert c.next == b
    assert b.next == a
    assert a.next == None

def test_reverse_list_1r():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # a -> b -> c -> d -> e -> f
    res = reverse_list_recursive(a)
    assert res == f
    assert f.next == e
    assert e.next == d
    assert d.next == c
    assert c.next == b
    assert b.next == a
    assert a.next == None

def test_reverse_list_2():
    x = Node("x")
    y = Node("y")
    x.next = y
    # x -> y
    res = reverse_list(x)
    assert res == y
    assert y.next == x
    assert x.next == None

def test_reverse_list_2r():
    x = Node("x")
    y = Node("y")
    x.next = y
    # x -> y
    res = reverse_list_recursive(x)
    assert res == y
    assert y.next == x
    assert x.next == None

def test_reverse_list_3():
    p = Node("p")
    # p
    res = reverse_list(p) # p
    assert res == p
    assert p.next == None

def test_reverse_list_3r():
    p = Node("p")
    # p
    res = reverse_list_recursive(p) # p
    assert res == p
    assert p.next == None

def test_reverse_list_4():
    assert reverse_list(None) is None
    assert reverse_list_recursive(None) is None
