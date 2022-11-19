# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        array = []
        self.inorder(root, array)
        minimum = float('inf')
        for i in range(1, len(array)):
            minimum = min(minimum, array[i] - array[i-1])
        return minimum
        
    def inorder(self, node, array):
        if not node: return
        self.inorder(node.left, array)
        array.append(node.val)
        self.inorder(node.right, array)
        return node
