# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Intuition
An inorder traversal of a BST visits nodes in strictly sorted (ascending) order.
So, if you record values during inorder, the list’s k‑th element (1‑indexed) is the k‑th smallest value.

Approach (what your code does)
Run a recursive DFS with inorder order:

Recurse left

Record root.val into ans

Recurse right

After traversal, ans is sorted; return ans[k‑1].

Complexity
Time: You visit every node once → O(n).

Space: ans stores all n values → O(n); recursion stack adds O(h), where h is height.
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans[k - 1]
