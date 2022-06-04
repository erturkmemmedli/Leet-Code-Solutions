# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.hash_table = set()
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return
        if root.val not in self.hash_table:
            self.hash_table.add(k - root.val)
        else:
            return True
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
