# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.List = []
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        self.List.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.List

# Alternative solution

class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        L = []
        def preorder(node):
            if not node: return
            L.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return L
