# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = 0
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root, None, None)
        return self.result   
        
    def dfs(self, node, parent, grandparent):
        if not node: return
        self.dfs(node.left, node, parent)
        if grandparent and grandparent.val % 2 == 0:
            self.result += node.val
        self.dfs(node.right, node, parent)
        return node
