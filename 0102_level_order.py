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
