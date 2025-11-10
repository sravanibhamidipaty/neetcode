"""
Edge Case: If length of s is not equal to length to t, return False

Intuition:
    Sort both the strings and see if they are equal
    TC: O(n log n + m log m) where n is the length of string s and
    m is the length of string t.
    SC: O(1) or O(n + m) depending on the sorting algorithm.

Approach:
    Have a counter array where I add characters of one
    string and subtract characters of another string.
    Return True if all the numbers in the counter array are 0
    and False otherwise.
    TC: O(n + m) where n is the length of string s and m is the
    length of string t.
    SC: O(1) since we have at most 26 characters.
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    character_counter = [0] * 26

    for i in range(len(s)):
        character_counter[ord(s[i])-ord('a')] += 1
        character_counter[ord(t[i])-ord('a')] -= 1

    for num in character_counter:
        if num != 0:
            return False

    return True