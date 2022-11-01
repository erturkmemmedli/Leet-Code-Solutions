# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maximumPathLength = 0
        self.dfs(root, None, None, 0)
        return self.maximumPathLength

    def dfs(self, node, parent, isLeft, path):
        self.maximumPathLength = max(self.maximumPathLength, path)
        if not node: return
        if isLeft == True:
            self.dfs(node.left, node, True, 0)
            self.dfs(node.right, node, False, path + 1)
        elif isLeft == False:
            self.dfs(node.left, node, True, path + 1)
            self.dfs(node.right, node, False, 0)
        else:
            self.dfs(node.left, node, True, path)
            self.dfs(node.right, node, False, path)
