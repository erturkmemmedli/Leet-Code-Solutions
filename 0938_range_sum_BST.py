# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.Sum = 0
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.Sum
        
    def dfs(self, root, low, high):
        if low <= root.val <= high:
            self.Sum += root.val    
        if root.left and root.val > low:
            self.dfs(root.left, low, high)
        if root.right and root.val < high:
            self.dfs(root.right, low, high)
        return
