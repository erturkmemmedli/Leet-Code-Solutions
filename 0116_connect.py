"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        Q = deque([deque([root]), deque([])])
        while Q:
            q = Q.popleft()
            while q:
                node = q.popleft()
                if q:
                    node.next = q[0]
                if node.left:
                    Q[0].append(node.left)
                if node.right:
                    Q[0].append(node.right)
                if not q:
                    if Q[0]:
                        Q.append(deque([]))
                    else:
                        break
        return root
