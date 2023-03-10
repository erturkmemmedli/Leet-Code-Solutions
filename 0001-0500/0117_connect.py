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

# Alternative solution

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        if root.left and root.right:
            root.left.next = root.right
        next = root.next
        while next and next.next:
            if not next.left and not next.right:
                next = next.next
            else:
                break
        if next:
            if root.right:
                if next.left:
                    root.right.next = next.left
                else:
                    root.right.next = next.right
            elif root.left:
                if next.left:
                    root.left.next = next.left
                else:
                    root.left.next = next.right
        right = self.connect(root.right)
        left = self.connect(root.left)
        return root
