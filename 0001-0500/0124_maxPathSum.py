# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -float("inf")
        self.dfs(root)
        return self.maxSum

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.maxSum = max(self.maxSum, left + right + node.val)
        res = max(max(left, right) + node.val, node.val)
        return res if res > 0 else 0
