# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.parentNode, self.firstProblemNode, self.secondProblemNode = None, None, None
        self.inorderDFS(root)
        temp = self.firstProblemNode.val
        self.firstProblemNode.val = self.secondProblemNode.val
        self.secondProblemNode.val = temp

    def inorderDFS(self, node):
        if not node: return
        self.inorderDFS(node.left)
        if self.parentNode and node.val < self.parentNode.val:
            if not self.firstProblemNode:
                self.firstProblemNode = self.parentNode
            self.secondProblemNode = node
        self.parentNode = node
        self.inorderDFS(node.right)
