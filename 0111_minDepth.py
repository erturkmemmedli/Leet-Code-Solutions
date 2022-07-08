# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.min = float('inf')
        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        height = 1
        self.dfs(root, height)
        return self.min
        
    def dfs(self, node, height):
        if not node.left and not node.right:
            self.min = min(self.min, height)
            return
        if node.left:
            self.dfs(node.left, height+1)
        if node.right:
            self.dfs(node.right, height+1)
