# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        self.path = []
        self.count = 0
        self.dfs(root, targetSum)
        return self.count

    def dfs(self, node, targetSum):
        if not node:
            return
        for i in range(len(self.path)):
            self.path[i] -= node.val
            if self.path[i] == 0: self.count += 1
        if targetSum - node.val == 0: self.count += 1
        self.path.append(targetSum - node.val)
        self.dfs(node.left, targetSum)
        self.dfs(node.right, targetSum)
        for i in range(len(self.path) - 1):
            self.path[i] += node.val
        self.path.pop()
