# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.moves = 0
        
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.postorder(root)
        return self.moves
    
    def postorder(self, root):
        if not root:
            return 0
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        self.moves += abs(left) + abs(right)
        return root.val + left + right - 1
        
# Alternative solution

class Solution1:
    def __init__(self):
        self.moves = 0
        
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.postorder(root)
        return self.moves
    
    def postorder(self, root):
        if root.left:
            root.val += self.postorder(root.left)
        if root.right:
            root.val += self.postorder(root.right)
        self.moves += abs(root.val - 1)
        return root.val - 1
