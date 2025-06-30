# Write a function, intersection, that takes in two lists,
#  a,_b_, as arguments. The function should return a new 
# list containing elements that are in both of the two lists.
# 
# You may assume that each input list does not contain duplicate elements.

# The simplest approach would be to have nested loops,
# the outer loop goes over the elements of a, while the inner loop
# goes over the elements of b. Whenever the elements match, they are added to our
# intersection list.
#
# Given that m is the length of a, and n is the length of b.
# we can say that:
#
# Time complexity: O(n*m)
# Space complexity: O(min(m,n))

def intersection(a,b):
    found = []
    for m in a:
        for n in b:
            if m == n:
                found.append(m)
                continue
    found.sort()
    return found

# The simple approach works, but it is inneficient. We could reduce the
# time complexity by using a data structure which would allow us to hash one
# of the lists. For example, a set. A set has a constant lookup time.
#
# Time complexity: O(n+m)
# Space complexity: O(min(m,n))
#
# By making use of a different data structure, we are able to decrease the
# time complexity, and the extra benefit in this case is that the space
# complexity remains unchanged.

def intersection_linear(a,b):
    map = set()
    map.update(a)
    found = []
    for item in b:
        if item in map:
            found.append(item)
    found.sort()
    return found


def test_intersection():
    assert intersection([4,2,1,6], [3,6,9,2,10]) == [2,6]
    assert intersection([2,4,6], [4,2]) == [2,4]
    assert intersection([4,2,1], [1,2,4,6]) == [1,2,4]

def test_intersection_linear():
    assert intersection_linear([4,2,1,6], [3,6,9,2,10]) == [2,6]
    assert intersection_linear([2,4,6], [4,2]) == [2,4]
    assert intersection_linear([4,2,1], [1,2,4,6]) == [1,2,4]