"""
Intuition
In a BST, all values in the left subtree are smaller than the node, and all in the right subtree are larger.
​
The LCA is the first node where the two target values “split” (one on each side) or hit exactly.
​

Approach (iterative)
Let cur = root.

While cur is not null:

If both p.val and q.val are less than cur.val, move left (cur = cur.left).
​

Else if both are greater than cur.val, move right (cur = cur.right).
​

Otherwise, cur is the LCA (either between them or equal to one).
​

Complexities
Time: O(h), where h is tree height;  O(logn) for balanced, O(n) for skewed.
​
Space: O(1) extra for iterative version; O(h) if written recursively (call stack).

"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
