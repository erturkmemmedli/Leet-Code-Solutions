# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result = "~"
        self.dfs(root, "")
        return self.result

    def dfs(self, node, path):
        if not node.left and not node.right:
            path += chr(97 + node.val)
            self.result = min(self.result, path[::-1])
            return
        if node.left:
            self.dfs(node.left, path + chr(97 + node.val))
        if node.right:
            self.dfs(node.right, path + chr(97 + node.val))
