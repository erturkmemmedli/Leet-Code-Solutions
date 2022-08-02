# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.dfs(root)
        return self.max
    
    def dfs(self, node):
        if not node:
          return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        left = l + 1 if node.left and node.val == node.left.val else 0
        right = r + 1 if node.right and node.val == node.right.val else 0
        self.max = max(self.max, left + right)
        return max(left, right)
