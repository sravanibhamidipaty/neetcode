"""
Intuition
We want the longest substring that can be turned into all one character using at most k replacements.

In any window, if we know the count of the most frequent character, then “everything else” in that window must be replaced.

So the key question per window is: “How many non-majority characters are there, and is that ≤ k?”​

Approach
Use a variable-size sliding window with two pointers left and right over the string.

Maintain a hashmap count of character frequencies in the current window and a max_freq = highest frequency of any char in the window.​

For each right, expand the window, update count[s[right]] and max_freq.

The window is valid if window_len - max_freq <= k because at most k replacements are needed to make all characters in the window the same.

While the window is invalid (window_len - max_freq > k), shrink from the left: decrement count[s[left]], move left forward.

After each expansion/shrink, update the answer with the current valid window length: ans = max(ans, right - left + 1).

Subtle but important: max_freq is monotonic non-decreasing (never reduced when shrinking). This is safe because it’s an upper bound on the true frequency; if a window is invalid with this upper bound, it’s definitely invalid with the real frequency.​

Time Complexity
O(n), where n is the length of the string.

Each character enters and leaves the window at most once; hashmap updates and checks are O(1).​

Space Complexity
O(1) extra space.

The hashmap stores counts for at most 26 uppercase letters, which is constant with respect to input size.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0)+1
            max_freq = max(max_freq, count[s[right]])

            while right-left+1-max_freq > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans