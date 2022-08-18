# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:    
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        self.dfs(root, dic)
        mxm = max(dic.values())
        return [key for key, val in dic.items() if val == mxm]
        
    def dfs(self, node, dic):
        if not node.left and not node.right:
            dic[node.val] += 1
            return
        if node.left:
            self.dfs(node.left, dic)
            node.val += node.left.val
        if node.right:
            self.dfs(node.right, dic)
            node.val += node.right.val
        dic[node.val] += 1
        return
