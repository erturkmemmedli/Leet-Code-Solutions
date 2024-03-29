# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.total = 0
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, root.val)
        return self.total
        
    def dfs(self, node, value):
        if not node.left and not node.right:
            self.total += value
            return
        if node.left:
            self.dfs(node.left, value * 10 + node.left.val)
        if node.right:
            self.dfs(node.right, value * 10 + node.right.val)    

# Alternative solution

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, node, pathSum):
        if not node:
            return 0
        pathSum += node.val
        if not node.left and not node.right:
            self.sum += pathSum
        self.dfs(node.left, 10 * pathSum)
        self.dfs(node.right, 10 * pathSum)
