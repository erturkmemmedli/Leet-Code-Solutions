# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.counter = {}
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        maximum = max(self.counter.values())
        output = []
        for k, v in self.counter.items():
            if v == maximum:
                output.append(k)
        return output
        
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        if root.val not in self.counter:
            self.counter[root.val] = 1
        else:
            self.counter[root.val] += 1
        self.inorder(root.right)
        return root
