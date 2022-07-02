# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.output = 0
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.tiltTree(root)
        return self.output
        
    def tiltTree(self, root):
        if not root.left and not root.right:
            return root
        elif not root.right:
            left = self.tiltTree(root.left)
            root.val += left.val
            self.output += abs(left.val)
        elif not root.left:
            right = self.tiltTree(root.right)
            root.val += right.val
            self.output += abs(right.val)
        else:
            left = self.tiltTree(root.left)
            right = self.tiltTree(root.right)
            root.val += left.val + right.val
            self.output += abs(left.val - right.val)
        return root
