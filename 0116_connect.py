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

# Alternative solution

from collections import deque

class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        queue = deque([[root]])
        while queue:
            level = queue.popleft()
            next_level = []
            for i, node in enumerate(level):
                if i + 1 < len(level):
                    node.next = level[i+1]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                queue.append(next_level)
        return root

# Alternative solution

class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
