# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sums = []
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.calculate(root)
        print(self.sums)
        vals = [self.sums[-1]]
        for i in range(1, len(self.sums)):
            vals.append(self.sums[-1] - self.sums[i-1])
        vals = vals[::-1]
        self.inorder(root, vals)
        return root
        
    def calculate(self, root):
        if not root: return
        self.calculate(root.left)
        if not self.sums: self.sums.append(root.val)
        else: self.sums.append(root.val + self.sums[-1])
        self.calculate(root.right)
        return root
    
    def inorder(self, root, vals):
        if not root: return
        self.inorder(root.left, vals)
        root.val = vals.pop()
        self.inorder(root.right, vals)
        return root

# Alternative solution

class Solution1:
    def __init__(self):
        self.summ = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.reverse_inorder(root)
        return root

    def reverse_inorder(self, root):
        if not root: return
        self.reverse_inorder(root.right)
        self.summ += root.val
        root.val = self.summ
        self.reverse_inorder(root.left)
        return root
