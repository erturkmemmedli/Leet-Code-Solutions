# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        string = ""
        self.dfs(root, string, result)
        return result
        
    def dfs(self, node, string, result):
        if not node.left and not node.right:
            string += str(node.val)
            result.append(string)
            return
        if node.left:
            self.dfs(node.left, string + str(node.val) + '->', result)
        if node.right:
            self.dfs(node.right, string + str(node.val) + '->', result)
