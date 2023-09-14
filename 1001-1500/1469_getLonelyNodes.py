# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.lonelyNodes = []
        self.dfs(root)
        return self.lonelyNodes
        
    def dfs(self, node):
        if not node:
            return
        if node.left and not node.right:
            self.lonelyNodes.append(node.left.val)
        if node.right and not node.left:
            self.lonelyNodes.append(node.right.val)
        self.dfs(node.left)
        self.dfs(node.right)
        return node
