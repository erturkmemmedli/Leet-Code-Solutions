# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.tree_height(root)
        m = height + 1
        n = 2 ** (height + 1) - 1
        matrix = [[""] * n for _ in range(m)]
        row = 0
        col = (n-1) // 2
        self.dfs(root, matrix, height, row, col)
        return matrix
        
    def tree_height(self, node):
        if not node:
            return -1
        return 1 + max(self.tree_height(node.left), self.tree_height(node.right))
    
    def dfs(self, node, matrix, height, row, col):
        if not node:
            return
        matrix[row][col] += str(node.val)
        self.dfs(node.left, matrix, height, row + 1, col - 2 ** (height - row - 1))
        self.dfs(node.right, matrix, height, row + 1, col + 2 ** (height - row - 1))
