# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        List = []
        Queue = deque([deque([root]), deque()])
        while Queue:
            q = Queue.popleft()
            if not q: break
            l = []
            while q:
                node = q.popleft()
                l.append(node.val)
                if node.left:
                    Queue[0].append(node.left)
                if node.right:
                    Queue[0].append(node.right)
            List.append(l)
            if Queue[0]:
                Queue.append(deque())
        return List

# Alternative solution

from collections import deque

class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        Q = deque([[root]])
        output = []
        while Q:
            level = Q.popleft()
            output.append([node.val for node in level])
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        levelOrder = []
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
            levelOrder.append(level)
        return levelOrder
