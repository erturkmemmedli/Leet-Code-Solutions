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
        zigzag = [[root]]
        reverse = 1
        while queue:
            level = queue.popleft()
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                queue.append(next_level)
                if reverse:
                    zigzag.append(next_level[::-1])
                else:
                    zigzag.append(next_level)
            reverse ^= 1
        zigzag = [[node.val for node in level] for level in zigzag]
        return zigzag
    
# Alternative solution

class Solution1:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        stack = [[root]]
        next_level = [root]
        reverse = 1
        while next_level:
            level = stack[-1]
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                stack.append(next_level)
            reverse ^= 1
        stack = [[node.val for node in level] if i % 2 == 0 else [node.val for node in level[::-1]] for i, level in enumerate(stack)]
        return stack
