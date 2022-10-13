"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution(object):
    def connect(self, root):
        if root is None:
            return
        Q = deque([deque([root])])
        while Q:
            if len(Q) == 1:
                Q.append(deque([]))
            if not len(Q[0]):
                break
            node = Q[0].popleft()
            if len(Q[0]):
                node.next = Q[0][0]
            else:
                Q.popleft()
            if node.left:
                Q[-1].append(node.left)
            if node.right:
                Q[-1].append(node.right)
        return root

# Alternative version

class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        queue = collections.deque([[root]])
        while queue:
            level = queue.popleft()
            nextLevel = []
            for i, node in enumerate(level):
                if i < len(level) - 1:
                    node.next = level[i+1]
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel:
                queue.append(nextLevel)
        return root
