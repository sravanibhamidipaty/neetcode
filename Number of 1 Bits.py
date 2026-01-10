"""
Intuition
Instead of checking every bit (including zeros), repeatedly remove the lowest set bit from n.
Each time you remove a set bit, you increment a counter; when there are no set bits left, the count equals the number of 1s.

Approach
Initialize count = 0.

While n != 0:

Do n &= (n - 1), which clears the rightmost 1‑bit in n.

Increment count by 1.

Return count as the number of 1 bits.

Time Complexity
The loop executes once per set bit.

Time complexity: O(number of set bits).

For fixed 32‑bit or 64‑bit integers, this is effectively O(1), but faster in practice than scanning every bit when the number is sparse.

Space Complexity
Uses a constant number of integer variables (n, count).

Extra space complexity: O(1).
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)   # clear lowest set bit
            count += 1
        return count