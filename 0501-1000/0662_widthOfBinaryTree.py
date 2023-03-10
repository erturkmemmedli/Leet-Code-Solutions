# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 1
        queue = collections.deque([[(root, 0)]])
        while queue:
            level = queue.popleft()
            nextLevel = []
            for node, index in level:
                if node.left:
                    nextLevel.append((node.left, 2 * index + 1))
                if node.right:
                    nextLevel.append((node.right, 2 * index + 2))
            if nextLevel:
                queue.append(nextLevel)
            if len(nextLevel) > 1:
                maxWidth = max(maxWidth, nextLevel[-1][1] - nextLevel[0][1] + 1)
        return maxWidth
