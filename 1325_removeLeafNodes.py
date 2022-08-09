# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.dfs(root, target)
        if root and not root.left and not root.right and root.val == target: return
        return root
        
    def dfs(self, node, target):
        if not node:
            return
        if not node.left and not node.right:
            return None if node.val == target else node
        node.left = self.dfs(node.left,  target)
        node.right = self.dfs(node.right, target)
        if not node.left and not node.right:
            return None if node.val == target else node
        else:
            return node
