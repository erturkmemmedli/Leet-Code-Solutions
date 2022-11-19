# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        result = []
        self.dfs(root, 0, result)
        return targetSum in result
        
    def dfs(self, root, Sum, result):
        if not root: return
        if not root.left and not root.right: result.append(Sum + root.val)
        self.dfs(root.left, Sum + root.val, result)
        self.dfs(root.right, Sum + root.val, result)

# Alternative solution

class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and root.val == targetSum: return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Alternative solution

class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        return self.helper(root, targetSum)
    
    def helper(self, root, x):
        if not root:
            return True if x == 0 else False
        if root.left and root.right:
            return self.helper(root.left, x - root.val) or self.helper(root.right, x - root.val)
        elif not root.right:
            return self.helper(root.left, x - root.val)
        elif not root.left:
            return self.helper(root.right, x - root.val)
