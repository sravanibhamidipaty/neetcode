from typing import List
"""
Intuition:
    Nested for loops and add the numbers to see if it is the target.
    TC: O(n^2)
    SC: O(1)

Approach:
    Hash map where key is the number and value is the index where the
    number is located.
    TC: O(n)
    SC: O(n)
"""

def twoSum(nums: List[int], target: int) -> List[int]:
    indices_map = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in indices_map:
            return [indices_map[diff], i]

        indices_map[nums[i]] = i
    return [-1, -1]