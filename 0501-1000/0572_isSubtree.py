# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot: return root == subRoot
        if root.val == subRoot.val and self.dfs(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, node, sub):
        if not node or not sub: return node == sub
        if node.val != sub.val: return False
        return self.dfs(node.left, sub.left) and self.dfs(node.right, sub.right)
