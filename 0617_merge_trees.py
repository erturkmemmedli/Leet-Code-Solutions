# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        Q = deque([(root1, root2)])
        while Q:
            node1, node2 = Q.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if not node1.left and node2.left:
                    node1.left = TreeNode(0)
                if not node1.right and node2.right:
                    node1.right = TreeNode(0)
                Q.append((node1.left, node2.left))
                Q.append((node1.right, node2.right))
        return root1
