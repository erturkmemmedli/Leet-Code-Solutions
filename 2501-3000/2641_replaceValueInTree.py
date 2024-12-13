# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([[root, None]])
        depth = 0

        while queue:
            level = queue.popleft()
            new_level = []
            level_sum = 0

            for node in level:
                if not node:
                    continue

                level_sum += node.val

                if node.left:
                    new_level.append(node.left)
                else:
                    new_level.append(None)

                if node.right:
                    new_level.append(node.right)
                else:
                    new_level.append(None)

            if new_level:
                queue.append(new_level)

                for i in range(0, len(level), 2):
                    if depth < 2:
                        if level[i]:
                            level[i].val = 0
                        if level[i+1]:
                            level[i+1].val = 0
                    else:
                        deletable = (level[i].val if level[i] else 0) + (level[i+1].val if level[i+1] else 0)
                        if level[i]:
                            level[i].val = level_sum - deletable
                        if level[i+1]:
                            level[i+1].val = level_sum - deletable

            depth += 1

        return root
