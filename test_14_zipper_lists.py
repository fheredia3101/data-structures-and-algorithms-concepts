# Write a function, zipper_lists, that takes in the head of
# two linked lists as arguments. The function should zipper
# the two lists together into single linked list by alternating
# nodes. If one of the linked lists is longer than the other,
# the resulting list should terminate with the remaining nodes.
# The function should return the head of the zippered linked list.
# 
# Do this in-place, by mutating the original Nodes.
# 
# You may assume that both input lists are non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Iterative approach.
# Time complexity: O(min(n, m))
# Space complexity: O(1)

def zipper_lists(head_1, head_2):
    current_1 = head_1
    current_2 = head_2
    count = 0
    while (current_1 is not None) and (current_2 is not None):
        print(f"count is {count}")
        if count % 2 == 0:
            next_1 = current_1.next
            current_1.next = current_2
            print(f"{current_1.val} now points to {current_2.val if current_2 else 'None'}")
            current_1 = next_1
            print(f"current_1 moves to {current_1.val if current_1 else 'None'}")
        else:
            next_2 = current_2.next
            current_2.next = current_1
            print(f"{current_2.val} now points to {current_1.val if current_1 else 'None'}")
            current_2 = next_2
            print(f"current_2 moves to {current_2.val if current_2 else 'None'}")
        count += 1
    return head_1

# Recursive approach
# Time complexity: O(max(m,n)) ? Not sure
# Space complexity: O(max(m,n)) ? Not sure

def zipper_lists_recursive(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists_recursive(next_1, next_2)
    return head_1

def print_list_recursive(head):
    if not head:
        return
    print(head.val)
    print_list_recursive(head.next)

def test_zipper_lists():
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

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    res = zipper_lists(a, x)
    assert res == a
    assert res.next == x
    assert x.next == b
    assert b.next == y
    assert y.next == c
    assert c.next == z
    assert z.next == d
    assert d.next == e
    assert e.next == f
    assert f.next == None

def test_zipper_lists_recursive():
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

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    res = zipper_lists_recursive(a, x)
    assert res == a
    assert res.next == x
    assert x.next == b
    assert b.next == y
    assert y.next == c
    assert c.next == z
    assert z.next == d
    assert d.next == e
    assert e.next == f
    assert f.next == None

