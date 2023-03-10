# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        Q = deque([[root]])
        level, depth, maxx = 0, 0, -float('inf')
        while Q:
            nodes = Q.popleft()
            level += 1
            next_nodes = []
            summ = 0
            for node in nodes:
                summ += node.val
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if summ > maxx:
                depth = level
                maxx = summ
            if next_nodes:
                Q.append(next_nodes)
        return depth
