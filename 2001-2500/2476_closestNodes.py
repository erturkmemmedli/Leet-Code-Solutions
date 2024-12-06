# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from bisect import bisect_left

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        output = []
        self.inorder = []
        self.dfs_inorder(root)

        for query in queries:
            idx = bisect_left(self.inorder, query)
            if idx < len(self.inorder) and self.inorder[idx] == query:
                output.append([query, query])
            elif idx == 0:
                output.append([-1, self.inorder[0]])
            elif idx == len(self.inorder):
                output.append([self.inorder[-1], -1])
            else:
                output.append([self.inorder[idx-1], self.inorder[idx]])

        return output
        
    def dfs_inorder(self, root):
        if not root: return
        self.dfs_inorder(root.left)
        self.inorder.append(root.val)
        self.dfs_inorder(root.right)

# Alternative solution (which gives TLE error)

from math import inf

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        self.output = []

        for query in queries:
            self.search(root, query, -1, -1)

        return self.output
        
    def search(self, root, target, minimum, maximum):
        if not root:
            self.output.append([minimum, maximum])
            return
        elif root.val == target:
            self.output.append([target, target])
            return
        elif root.val > target:
            self.search(root.left, target, minimum, root.val)
        else:
            self.search(root.right, target, root.val, maximum)
