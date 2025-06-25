# Write a function, pair_sum, that takes in a list and a target sum as arguments.
# The function should return a tuple containing a pair of indices whose elements
# sum to the given target. The indices returned must be unique.
#
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair that sums to the target.
#
# The simple approach would be to check every combination by brute force.
# This results in two nested loops.
# Time complexity: O(n^2)
# Space complexity: O(1)

def pair_sum(numbers, sum):

    indices = None
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                indices = (i,j)
    return indices

# The optimized approach reduces the time complexity to linear.
# As we traverse our list, we keep track of the objects that we have seen,
# as well as the index where we can find it. This history is stored in a hash
# map.
#
# Now comes the magic element: When we look at each element of the list, 
# we will check if its complement exist in the history we have been
# keeping track of. If it does, we return the index of the current element, and
# the index of its complement, convieniently stored in our history.
#
# This solution comes at a tradeoff, time complexity is reduced while space
# complexity is increased.
#
# Time complexity: O(n)
# Space complexity: O(n)

def pair_sum_linear(numbers, sum):
    history = {}
    for i in range(len(numbers)):
        complement = sum - numbers[i]
        if complement in history:
            return (i, history[complement])
        else:
            history[numbers[i]] = i
    return ()


def test_pair_sum():
    assert pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
    assert pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
    assert pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
    assert pair_sum([4, 7, 9, 2, 1, 1], 2) # -> (3, 5)

def test_pair_sum_linear():
    assert pair_sum_linear([3, 2, 5, 4, 1], 8) # -> (0, 2)
    assert pair_sum_linear([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
    assert pair_sum_linear([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
    assert pair_sum_linear([4, 7, 9, 2, 1, 1], 2) # -> (3, 5)