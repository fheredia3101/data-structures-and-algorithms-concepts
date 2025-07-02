# Write a function sum_numbers_recursive that takes in an
# array of numbers and returns the sum of all the numbers
# in the array.
# All elements will be integers. Solve this recursively.
#
# This could be solved using simpler methods, like a for loop.
# However the purpose is to learn about recursion.
#
# We will solve this by taking the first element of the list,
# and creating a recursive call to get the sum of the remaining elements.
#
# For example, given the list = [3, 7, 12]
# The steps will be as follows:
# sum([3, 7, 12])
#   3 + sum([7, 12])
#     3 + 7 + sum([12])
#       3 + 7 + 12 + sum([])
#
# Note that our base case here is sum([]) and it should return 0.
#
# The time and spae complexities are calculated by a) the
# amount of recursive calls and b) the steps taken on each
# recursive step.
#
# Time complexity: O(n^2)
# n given the recursive calls, another n due to the list slicing.
# 
# Space complexity: O(n^2)
# Every step (n) we create a sublist. The size of it ranges from n to 0.
# The average list size is then n/2 , but simplifying it gives us simply n.
# Thus, n * n.

def sum_numbers_recursive(numbers):
    if not numbers:
        # Base case: List empty
        return 0
    # Recursive step: get the first element out.
    # make a call with remaining elements.
    return numbers[0] + sum_numbers_recursive(numbers[1:])

def test_sum_numbers_recursive():
    assert sum_numbers_recursive([5, 2, 9, 10]) == 26
    assert sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]) == 1
    assert sum_numbers_recursive([]) == 0
    assert sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]) == 1001