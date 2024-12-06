# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.start_node = None

        def assign_parent(node, parent):
            if not node:
                return
            
            if node.val == start:
                self.start_node = node

            node.parent = parent
            assign_parent(node.left, node)
            assign_parent(node.right, node)

        assign_parent(root, None)
        visited = {start}
        queue = deque([self.start_node])
        time = -1

        while queue:
            l = len(queue)
            time += 1

            for i in range(l):
                node = queue.popleft()

                if node.left and node.left.val not in visited:
                    visited.add(node.left.val)
                    queue.append(node.left)
                if node.right and node.right.val not in visited:
                    visited.add(node.right.val)
                    queue.append(node.right)
                if node.parent and node.parent.val not in visited:
                    visited.add(node.parent.val)
                    queue.append(node.parent)

        return time
