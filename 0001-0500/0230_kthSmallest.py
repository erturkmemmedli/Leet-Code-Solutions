# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.list = []
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root, k)
        return self.list[-1]
        
    def inorder(self, node, k):
        if not node: return
        self.inorder(node.left, k)
        if len(self.list) == k: return
        self.list.append(node.val)
        self.inorder(node.right, k)
