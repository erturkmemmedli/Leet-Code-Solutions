# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        tree = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.traversal(tree, preorder[i])
        return tree
        
    def traversal(self, tree, val):
        if not tree:
            return TreeNode(val)
        if val < tree.val:
            tree.left = self.traversal(tree.left, val)
        if val > tree.val:
            tree.right = self.traversal(tree.right, val)
        return tree
