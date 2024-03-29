# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        Q = deque([[root]])
        output = deque()
        while Q:
            level = Q.popleft()
            output.appendleft([node.val for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                Q.append(next_level)
        return output

# Alternative solution

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        levelOrder = deque()
        while queue:
            levelSize = len(queue)
            level = []
            for _ in range(levelSize):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levelOrder.appendleft(level)
        return levelOrder
