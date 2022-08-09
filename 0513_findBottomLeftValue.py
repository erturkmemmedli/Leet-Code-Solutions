# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        Q = deque([[root]])
        while Q:
            level = Q.popleft()
            leftmost = level[0].val
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if new_level:
                Q.append(new_level)
        return leftmost
