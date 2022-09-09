# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue = deque([[root]])
        zigzag = [[root.val]]
        reverse = 1
        while queue:
            level = queue.popleft()
            next_level = []
            next_zigzag = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                    next_zigzag.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    next_zigzag.append(node.right.val)
            if next_level:
                queue.append(next_level)
                if reverse:
                    zigzag.append(next_zigzag[::-1])
                else:
                    zigzag.append(next_zigzag)
            reverse ^= 1
        return zigzag
