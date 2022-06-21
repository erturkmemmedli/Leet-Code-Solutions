# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        val = str(root.val)
        left = '(' + self.tree2str(root.left) + ')'
        right = '(' + self.tree2str(root.right) + ')'
        if root.left and root.right:
            return val + left + right
        if not root.left and root.right:
            return val + '()' + right
        if root.left and not root.right:
            return val + left
        if not root.left and not root.right:
            return val
