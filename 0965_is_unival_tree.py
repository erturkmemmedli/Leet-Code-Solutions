# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.flag = True
        
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        result = self.dfs(root, val)
        return self.flag
        
    def dfs(self, node, val):
        if self.flag:
            if node:
                if node.val != val:
                    self.flag = False
                self.dfs(node.left, val)
                self.dfs(node.right, val)

# Alternative solution

class Solution1:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        result = self.dfs(root, val)
        return result
        
    def dfs(self, node, val):
        if not node:
            return True
        else:
            if node.val != val:
                return False
            return self.dfs(node.left, val) and self.dfs(node.right, val)
