# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return
        output = []
        self.dfs(root, targetSum, output, [root.val], root.val)
        return output
    
    def dfs(self, node, target, output, path, pathSum):
        if not node.left and not node.right:
            if target == pathSum:
                output.append(path)
            return
        if node.left:
            self.dfs(node.left, target, output, path + [node.left.val], pathSum + node.left.val)
        if node.right:
            self.dfs(node.right, target, output, path + [node.right.val], pathSum + node.right.val)

# Alternative solution

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.paths = []
        path = [root.val]
        self.dfs(root, targetSum, path)
        return self.paths
        
    def dfs(self, node, targetSum, path):
        if not node:
            return
        targetSum -= node.val
        if not node.left and not node.right and targetSum == 0:
            self.paths.append(path)
            return
        if node.left:
            self.dfs(node.left, targetSum, path + [node.left.val])
        if node.right:
            self.dfs(node.right, targetSum, path + [node.right.val])

# Alternative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        def dfs(root, target, path):
            if not root:
                return

            if not root.right and not root.left:
                if target == root.val:
                    path.append(root.val)
                    output.append(path[:])
                    path.pop()
                return
            
            path.append(root.val)
            dfs(root.left, target - root.val, path)
            dfs(root.right, target - root.val, path)
            path.pop()

        dfs(root, targetSum, [])
        return output
