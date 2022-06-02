# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        result = []
        self.dfs(root, 0, result)
        return targetSum in result
        
    def dfs(self, root, Sum, result):
        if not root: return
        if not root.left and not root.right: result.append(Sum + root.val)
        self.dfs(root.left, Sum + root.val, result)
        self.dfs(root.right, Sum + root.val, result)
