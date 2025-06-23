
# Write a function, most_frequent_char, that takes
# in a string as an argument. The function should
# return the most frequent character of the string.
# If there are ties, return the character that appears
# earlier in the string.
#
# You can assume that the input string is non-empty.
#
# Similar to the anagrams example, we will create a dictionary
# that contains the present characters and their count of
# appearances.
# 
# Once that structure is built, we need to find the character
# that has the highest count AND appears earlies in case of a tie.
#
# Time complexity: O(n)
# Space complexity: O(n)

def build_character_count(input):
    character_count = {}
    for c in input:
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] = character_count[c] + 1
    return character_count

def most_frequent_char(input):
    character_count = build_character_count(input)
    most_frequent_char = None
    for c in input:
        if not most_frequent_char:
            most_frequent_char = c
        else:
            if character_count[c] > character_count[most_frequent_char]:
                most_frequent_char = c
    return most_frequent_char


def test_most_frequent_char():
    assert most_frequent_char('bookeeper') == 'e'
    assert most_frequent_char('david') == 'd'
    assert most_frequent_char('abby') == 'b'
    assert most_frequent_char('mississippi') == 'i'