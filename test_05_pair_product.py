# Write a function, pair_product, that takes in a list and
# a target product as arguments. The function should return
# a tuple containing a pair of indices whose elements multiply
# to the given target. The indices returned must be unique.
#
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair whose product is the target.
#
# This is a similar problem than the pair sum, only the operation changes.
# Namely, a multiplication instead of a sum.
#
# The simplest approach would be to have nested loops and find the two factors.
# But in a similar way to pair sum, we can optimize to a linear algorithm by
# keeping track of our history, and looking for the _complement_ of each entry
# in the list. What a complement is, depends on the operation that is required.
# In this specific case, we are looking for the factors of a target product.
#
# Time complexity: O(n)
# Space complexity: O(n)

def pair_product(numbers, target):
    history = {}
    for i, num in enumerate(numbers):
        complement = target / num
        if complement in history:
            return (history[complement], i)
        # complement not found, update history
        history[num] = i


def test_pair_product():
    assert pair_product([3, 2, 5, 4, 1], 8) == (1, 3)
    assert pair_product([3, 2, 5, 4, 1], 10) == (1, 2)
    assert pair_product([4, 7, 9, 2, 5, 1], 5) == (4, 5)