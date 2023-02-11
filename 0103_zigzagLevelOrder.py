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
   
# Alternative solution

from collections import deque

class Solution1:
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

class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        stack = [[root]]
        next_level = [root]
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
        stack = [[node.val for node in level] if i % 2 == 0 else [node.val for node in level[::-1]] for i, level in enumerate(stack)]
        return stack

# Alternative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        levelOrder = []
        reverse = 0
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
            levelOrder.append(level[::-1] if reverse else level)
            reverse ^= 1
        return levelOrder
