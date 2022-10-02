# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.postorder_num = defaultdict(int)
        self.postorder_node = defaultdict(TreeNode)
        self.dfs(root)
        result = []
        for key, val in self.postorder_num.items():
            if val > 1:
                result.append(self.postorder_node[key])
        return result

    def dfs(self, node):
        if not node: return "N"
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        tree = left + "Y" + right + "Y" + str(node.val)
        self.postorder_num[tree] += 1
        self.postorder_node[tree] = node
        return tree
