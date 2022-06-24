# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.flag = False
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return False if self.flag else True
        
    def height(self, node): 
        if not node: return 0
        left = self.height(node.left)
        right = self.height(node.right)
        if abs(left - right) > 1: self.flag = True
        return 1 + max(left, right)
