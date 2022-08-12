# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (root1 and not root2) or (not root1 and root2) or (root1 and root2 and root1.val != root2.val):
            return False
        if not root1 and not root2:
            return True
        l1 = root1.left
        r1 = root1.right
        l2 = root2.left
        r2 = root2.right
        return (self.flipEquiv(l1, r2) or self.flipEquiv(l1, l2)) and (self.flipEquiv(r1, r2) or self.flipEquiv(r1, l2))
