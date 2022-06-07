"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children: return 1
        return max([1 + self.maxDepth(child) for child in root.children])
      
# Alternative solution

from collections import deque

class Solution1:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children: return 1
        depth = 1
        Q = deque(root.children)
        children = []
        while Q:
            child = Q.popleft()
            if child.children:
                children += child.children
            if not Q:
                depth += 1
                if children:
                    Q = deque(children)
                children = []
        return depth
