# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return
        output = []
        self.dfs(root, targetSum, output, [root.val], root.val)
        return output
    
    def dfs(self, node, target, output, path, pathSum):
        if not node.left and not node.right:
            if target == pathSum:
                output.append(path)
            return
        if node.left:
            self.dfs(node.left, target, output, path + [node.left.val], pathSum + node.left.val)
        if node.right:
            self.dfs(node.right, target, output, path + [node.right.val], pathSum + node.right.val)
