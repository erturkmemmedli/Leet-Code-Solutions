# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([[root]])
        isOdd = False

        while queue:
            level = queue.popleft()

            if isOdd:
                vals = [n.val for n in level]
                for i in range(len(level)):
                    level[i].val = vals[-i-1]

            new_level = []
            isOdd ^= True

            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
                else:
                    break
            else:
                queue.append(new_level)

        return root
