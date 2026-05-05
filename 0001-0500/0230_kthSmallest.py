# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.list = []
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root, k)
        return self.list[-1]
        
    def inorder(self, node, k):
        if not node: return
        self.inorder(node.left, k)
        if len(self.list) == k: return
        self.list.append(node.val)
        self.inorder(node.right, k)

# Alternative solution

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count_nodes(root)
        return self.dfs(root, k)
    
    def count_nodes(self, root):
        if not root:
            return 0
        root.count = 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
        return root.count

    def dfs(self, root, k):
        if not root.left and k - 1 == 0:
            return root.val
        if root.left and root.left.count == k - 1:
            return root.val
        if root.left and root.left.count > k - 1:
            return self.dfs(root.left, k)
        if root.right:
            return self.dfs(root.right, k - root.count + root.right.count)
