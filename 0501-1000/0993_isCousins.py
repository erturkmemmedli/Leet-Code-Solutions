# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        Q = deque([[root]])
        while Q:
            level = Q.popleft()
            nodes = []
            vals = set()
            for node in level:
                if node.left and node.right:
                    if node.left.val in [x,y] and node.right.val in [x,y]:
                        return False
                if node.left:
                    nodes.append(node.left)
                    vals.add(node.left.val)
                if node.right:
                    nodes.append(node.right)
                    vals.add(node.right.val)
            if x in vals and y in vals:
                return True
            if nodes: Q.append(nodes)
        return False
