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

# Alternative solution

class Solution1: 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
        
    def dfs(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        if left.val == right.val:
            outer = self.dfs(left.left, right.right)
            inner = self.dfs(left.right, right.left)
            if outer and inner: return True
            else: return False
           
# Alternative solution

class Solution2: 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [[root.left, root.right]]
        while stack:
            left, right = stack.pop()
            if not left and not right: continue
            if not left or not right: return False
            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            else:
                return False
        return True
