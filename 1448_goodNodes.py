# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 1
    
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return self.count
        if root.left:
            if root.left.val >= root.val:
                self.count += 1
            else:
                root.left.val = root.val
            self.goodNodes(root.left)
        if root.right:
            if root.right.val >= root.val:
                self.count += 1
            else:
                root.right.val = root.val
            self.goodNodes(root.right)
        return self.count
