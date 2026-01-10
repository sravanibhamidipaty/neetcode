"""
Intuition
You want to read the bits of n from right to left and rebuild a new number from left to right.
Each step: shift your result left to “make room” and then drop in the current least‑significant bit of n.

Approach
Initialize res = 0.

Repeat 32 times (for a 32‑bit integer):

Shift res left by 1 bit.

Take the lowest bit of n with n & 1 and add it to res.

Shift n right by 1 to move to the next bit.

Return res as the reversed‑bit integer.

Time Complexity
Loop runs a fixed 32 times → O(1) time for 32‑bit integers.

Space Complexity
Uses only a few integer variables → O(1) extra space.

res |= (n & 1) is a bitwise OR‑and‑assign step.
​

n & 1 extracts the current least significant bit of n (either 0 or 1).

res |= x is shorthand for res = res | x, so this line sets the last bit of res to that extracted bit without changing the others.
​

So after res <<= 1 makes room, res |= (n & 1) “drops in” the next bit of the reversed number.
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1            # make room for next bit
            res |= (n & 1)       # add current least-significant bit
            n >>= 1              # move to next bit
        return res