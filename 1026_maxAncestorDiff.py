# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maximum = 0
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        mxm = - float('inf')
        mnm = float('inf')
        self.traverse(root, mxm, mnm)
        return self.maximum
        
    def traverse(self, node, mxm, mnm):
        if not node:
            return
        tmp = [mxm, mnm]
        if node.left:
            mxm = max(mxm, max(node.val, node.left.val))
            mnm = min(mnm, min(node.val, node.left.val))
            self.maximum = max(self.maximum, abs(mxm-mnm))
            left = self.traverse(node.left, mxm, mnm)
        if node.right:
            mxm = max(tmp[0], max(node.val, node.right.val))
            mnm = min(tmp[1], min(node.val, node.right.val))
            self.maximum = max(self.maximum, abs(mxm-mnm))
            right = self.traverse(node.right, mxm, mnm)
        return node
        
