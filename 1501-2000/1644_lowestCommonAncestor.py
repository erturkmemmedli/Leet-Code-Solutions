# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_found = False
        self.q_found = False
        lca = self.find_LCA(root, p, q) 
        if self.p_found and self.q_found:
            return lca
        elif self.p_found:
            return lca if self.find_node(lca, q) else None
        elif self.q_found:
            return lca if self.find_node(lca, p) else None
        else:
            return None
        
    def find_node(self, node, target):
        if not node:
            return False
        if node == target:
            return True
        
        return self.find_node(node.left, target) or self.find_node(node.right, target)


    def find_LCA(self, root, p, q):
        if not root:
            return

        if root == p or root == q:
            if root == p:
                self.p_found = True
            if root == q:
                self.q_found = True
            return root

        left = self.find_LCA(root.left, p, q)
        right = self.find_LCA(root.right, p, q)

        if left and right:
            return root

        elif left:
            return left

        elif right:
            return right
