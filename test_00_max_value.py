# Write a function, max_value, that takes in a list of numbers as an argument. The function should return the largest number in the list.
# Solve this without using any built-in list methods.
# You can assume that the list is non-empty.
#
# max_value([4, 7, 2, 8, 10, 9]) # -> 10
# max_value([10, 5, 40, 40.3]) # -> 40.3
# max_value([-5, -2, -1, -11]) # -> -1
#
# Time complexity: O(n)
# Space complexity: O(1)
#
import pytest

def max_value(nums):
    result = float('-inf')
    for num in nums:
        if num > result:
            result = num
    return result

def test_max_value():
    assert max_value([4, 7, 2, 8, 10, 9]) == 10
    assert max_value([10, 5, 40, 40.3]) == 40.3
    assert max_value([-5, -2, -1, -11]) == -1