# Write a function, is_prime, that takes in a number as an argument.
# The function should return a boolean indicating whether or not the given number is prime.

# A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

# For example, 7 is a prime because it is only divisible by 1 and 7.
# For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

# You can assume that the input number is a positive integer.

from math import sqrt, floor

# The simplest solution is to iterate through all numbers between 2 and input - 1
# If input can be divided by any of these numbers, then input is not prime.
# Time complexity : O(n)
# Space complexity: O(1)
def is_prime(input):
    if input < 2:
        return False
    for i in range(2, input):
        if input % i == 0:
            return False
    return True

# When finding a prime number, we want to know if the
# multiplication of factors other than 1 and input would
# give input as a result.
# This is possible to determine if we assume that the
# factors come in pairs. As we traverse the lower numbers,
# we would reach a point at which the factors would reverse; this
# point is given by the number's square root.
# Therefore, if we haven't found divisors for input when we reach
# input's square root (rounding up just in case), then it can be
# considered that input is indeed a prime number
def is_prime_optimized(input):
    if input < 2:
        return False
    upper_limit = int(floor(sqrt(input)) + 1)
    for i in range(2, upper_limit):
        if input % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(64) is False

def test_is_prime_optimized():
    assert is_prime_optimized(0) is False
    assert is_prime_optimized(1) is False
    assert is_prime_optimized(2) is True
    assert is_prime_optimized(7) is True
    assert is_prime_optimized(64) is False