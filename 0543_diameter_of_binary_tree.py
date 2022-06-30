# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maximum = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        left = root.left
        right = root.right
        self.maximum = max(self.maximum, self.calculate(left) + self.calculate(right))
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.maximum
        
    def calculate(self, node):
        if not node:
            return 0
        return 1 + max(self.calculate(node.left), self.calculate(node.right))
      
# Alternative solution

class Solution1:
    def __init__(self):
        self.maximum = 0
        self.hashtable = {}
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculate(root)
        self.dfs(root)
        return self.maximum        
    
    def dfs(self, node):
        if not node.left and not node.right:
            return 0
        elif not node.right:
            self.maximum = max(self.maximum, self.hashtable[node.left])
        elif not node.left:
            self.maximum = max(self.maximum, self.hashtable[node.right])
        else:
            self.maximum = max(self.maximum, self.hashtable[node.left] + self.hashtable[node.right])
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)
        return
        
    def calculate(self, node):
        if not node:
            return 0
        val = 1 + max(self.calculate(node.left), self.calculate(node.right))
        self.hashtable[node] = val
        return val
