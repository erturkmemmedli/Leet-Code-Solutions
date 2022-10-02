# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        Q = deque([root])
        curr = depth - 2
        while curr:
            for _ in range(len(Q)):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            curr -= 1
        for node in Q:
            left = node.left if node.left else None
            right = node.right if node.right else None
            node.left = TreeNode(val)
            node.left.left = left
            node.right = TreeNode(val)
            node.right.right = right
        return root
