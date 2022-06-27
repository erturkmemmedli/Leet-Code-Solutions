# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.list = []
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        minimum = float('inf')
        for i in range(1, len(self.list)):
            minimum = min(minimum, self.list[i] - self.list[i-1])
        return minimum
        
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.list.append(node.val)
        self.dfs(node.right)
        
# Alternative solution

class Solution1:
    def __init__(self):
        self.previous = -float('inf')
        self.result = float('inf')
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.previous)
        self.previous = root.val
        self.minDiffInBST(root.right)
        return self.result
