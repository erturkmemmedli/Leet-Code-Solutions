# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        height = 0
        Q = deque([deque([root]), deque()])
        while Q:
            q = Q.popleft()
            if not q: break
            height += 1
            while q:
                node = q.popleft()
                if node.left:
                    Q[0].append(node.left)
                if node.right:
                    Q[0].append(node.right)
            if Q[0]:
                Q.append(deque())
        return height

# Alternative solution

class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

# Alternative solution

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
