# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.tree = []
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        new_root = self.list_to_tree(self.tree, len(self.tree))
        return new_root
        
    def inorder(self, node):
        if not node:return
        self.inorder(node.left)
        self.tree.append(node.val)
        self.inorder(node.right)
        
    def list_to_tree(self, tree, l):
        if not l: return
        elif l == 1: return TreeNode(tree[0])
        m = l // 2
        root = TreeNode(tree[m])
        root.left = self.list_to_tree(tree[:m], m)
        root.right = self.list_to_tree(tree[m+1:], l-m-1)
        return root
