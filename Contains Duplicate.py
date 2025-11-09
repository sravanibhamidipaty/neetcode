from typing import List

"""
Intuition: 
    Sort the array and see if the previous number is the same as the correct number. 
    TC: O(n log n) 
    SC: O(n) or O(1) depending on the sorting algorithm

Approach: 
    Use a hash set to store the numbers that are already seen. 
    Return true if the number is seen already. 
    Return False at the end because it means that the no duplicates are found. 
    TC: O(n) 
    SC: O(n)
"""

def hasDuplicate(nums: List[int]) -> bool:
    hasSeen = set()

    for num in nums:
        if num in hasSeen:
            return True
        hasSeen.add(num)

    return False
