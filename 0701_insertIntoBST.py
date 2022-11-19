# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        if val < root.val:
            if root.left:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
            return root
        if val > root.val:
            if root.right:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
            return root

# Alternative solution

class Solution1:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root
