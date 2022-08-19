# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.deepest = 0
        self.lca = None
        
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root, 0)
        return self.lca
        
    def dfs(self, node, depth):
        self.deepest = max(self.deepest, depth)
        if not node:
            return depth
        left = self.dfs(node.left, depth + 1)
        right = self.dfs(node.right, depth + 1)
        if left == right == self.deepest:
            self.lca = node
        return max(left, right)
      
# Alternative solution

class Solution1:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)[1]
        
    def dfs(self, node):
        if not node:
            return 0, None
        depth1, lca1 = self.dfs(node.left)
        depth2, lca2 = self.dfs(node.right)
        if depth1 > depth2: return depth1 + 1, lca1
        if depth1 < depth2: return depth2 + 1, lca2
        return depth1 + 1, node
