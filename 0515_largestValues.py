# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import sys

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        Q = deque([[root]])
        largest = [root.val]
        while Q:
            level = Q.popleft()
            new_level = []
            maximum = - sys.maxsize - 1
            for node in level:
                if node.left:
                    new_level.append(node.left)
                    maximum = max(maximum, node.left.val)
                if node.right:
                    new_level.append(node.right)
                    maximum = max(maximum, node.right.val)
            if new_level:
                largest.append(maximum)
                Q.append(new_level)
        return largest
