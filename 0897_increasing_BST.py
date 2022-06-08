# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tree = []
        self.inorder(root, tree)
        node = tree[0]
        temp = node
        for i in range(1, len(tree)):
            temp.left = None
            temp.right = tree[i]
            temp = tree[i]
        temp.left = None
        temp.right = None
        return node
        
    def inorder(self, root, tree):
        if not root: return
        self.inorder(root.left, tree)
        tree.append(root)
        self.inorder(root.right, tree)
        return root
      
# Alternative solution

class Solution1:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[0]
        
    def dfs(self, node):
        left1, right2 = node, node
        if node.left:
            left1, left2 = self.dfs(node.left)
            left2.right = node
        if node.right:
            right1, right2 = self.dfs(node.right)
            node.right = right1
        node.left = None
        return left1, right2    
