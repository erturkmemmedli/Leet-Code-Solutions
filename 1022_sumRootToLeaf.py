# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        bin_str = ""
        store = []
        self.dfs(root, bin_str ,store)
        return sum([int(i, 2) for i in store])
        
    def dfs(self, node, bin_str, store):
        bin_str += str(node.val)
        if not node.left and not node.right:
            store.append(bin_str)
            return
        if node.left:
            self.dfs(node.left, bin_str, store)
        if node.right:
            self.dfs(node.right, bin_str, store)
