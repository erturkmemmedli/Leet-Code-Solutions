# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.list = []
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preorder(root)
        for i in range(len(self.list) - 1):
            self.list[i].right = self.list[i+1]
            self.list[i].left = None
        
    def preorder(self, node):
        if not node: return
        self.list.append(node)
        self.preorder(node.left)
        self.preorder(node.right)
        
# Alternative solution

class Solution1:
    def __init__(self):
        self.prev = None
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
