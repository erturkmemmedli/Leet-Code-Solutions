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

# Alternative solution

class Solution1:
    def __init__(self):
        self.hashset = set()
        self.flag = False
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not self.flag:
            if root.val in self.hashset:
                self.flag = True
            else:
                self.hashset.add(k - root.val)
                if root.left: self.findTarget(root.left, k)
                if root.right: self.findTarget(root.right, k)        
        return self.flag
