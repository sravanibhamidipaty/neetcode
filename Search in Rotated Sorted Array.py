"""
Intuition
The array was sorted, then rotated, so at any time at least one half (left or right) of [left, mid, right] is still sorted.

If a half is sorted, it is easy to check if the target lies inside that half by comparing to its endpoints.

Use this to decide which half to discard each step, while doing a standard binary search.​

Approach
Maintain left = 0, right = n - 1.

While left <= right:

Compute mid = (left + right) // 2.

If nums[mid] == target, return mid.

Decide which half is sorted:

If nums[left] <= nums[mid], then left half is sorted.

If nums[left] <= target < nums[mid], target is in left half → right = mid - 1.

Else, target is in right half → left = mid + 1.

Else, right half is sorted.

If nums[mid] < target <= nums[right], target is in right half → left = mid + 1.

Else, target is in left half → right = mid - 1.

If the loop ends, return -1 (target not found).

Key phrase: “On each step I identify which half is sorted, check if the target falls in that sorted interval, and then discard the other half. That preserves binary-search O(log n) time even with rotation.”​

Time Complexity
Each iteration halves the search space O(log n).

Space Complexity
Only a few indices and variables O(1) extra space.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
