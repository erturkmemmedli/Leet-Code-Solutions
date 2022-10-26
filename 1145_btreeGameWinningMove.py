# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        redNode = self.dfs(root, x)
        left = self.size(redNode.left)
        right = self.size(redNode.right)
        total = left + right + 1
        return n - total > total or left > n - left or right > n - right

    def dfs(self, node, x):
        if not node:
            return
        if node.val == x:
            return node
        return self.dfs(node.left, x) or self.dfs(node.right, x)

    def size(self, node):
        if not node:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
