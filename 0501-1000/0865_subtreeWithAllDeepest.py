# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        Queue = deque([[root]])
        root.parent = None
        while Queue:
            level = Queue.popleft()
            next_level = []
            for node in level:
                if node.left:
                    node.left.parent = node
                    next_level.append(node.left)
                if node.right:
                    node.right.parent = node
                    next_level.append(node.right)
            if next_level:
                Queue.append(next_level)
        while len(level) > 1:
            parent = set()
            for node in level:
                parent.add(node.parent)
            level = parent
        return level.pop()
