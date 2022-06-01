# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        List = []
        multiplier = 10
        self.inorder(root, List, multiplier)
        for i in range(len(List) // 2):
            if List[i] != List[len(List) - 1 - i]:
                return False
        return True
        
    def inorder(self, node, arr, multiplier):
        if not node: return
        self.inorder(node.left, arr, multiplier * 10)
        node.val *= multiplier
        arr.append(node.val)
        self.inorder(node.right, arr, multiplier * 10)
        return arr
