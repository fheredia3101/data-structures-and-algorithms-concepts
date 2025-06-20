# Write a function, anagrams,
# that takes in two strings as arguments.
# The function should return a boolean indicating whether
# or not the strings are anagrams. Anagrams are strings
# that contain the same characters, but in any order.
#
# When it comes to anagrams, the order of the characters is
# irrelevant. They should only have the exact same character count.
#
# A dictionary can be a good data strcuture to use here, where
# the key is the character, and the value is the count of
# appearances for such character.
#
# Time complexity:  O(n + m)
# Space complexity: O(n + m)
#
# where
# n: length of first string
# m: length of second string

def anagrams(first, second):
    # Build first dictionary
    first_map = {}
    for c in first:
        if c not in first_map:
            first_map[c] = 1
        else:
            first_map[c] = first_map[c] + 1
    # Build second dictionary
    second_map = {}
    for c in second:
        if c not in second_map:
            second_map[c] = 1
        else:
            second_map[c] = second_map[c] + 1
    # Compare key-value pairs. True if exact match.
    return first_map == second_map

def test_anagrams():
    assert anagrams('restful', 'fluster') # True
    assert not anagrams('cats', 'tocs')   # False
    assert anagrams('monkeyswrite', 'newyorktimes') # True
    assert not anagrams('paper', 'reapa') # False