# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.thief_path(root))
    
    def thief_path(self, node):
        if not node:
            return (0, 0)
        left = self.thief_path(node.left)
        right = self.thief_path(node.right)
        current = node.val + left[1] + right[1]
        previous = max(left) + max(right)
        return (current, previous)
