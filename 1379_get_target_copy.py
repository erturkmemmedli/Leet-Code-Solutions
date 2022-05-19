# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        Q1 = deque([original])
        Q2 = deque([cloned])
        while Q1:
            pop1 = Q1.popleft()
            pop2 = Q2.popleft()
            if pop1 == target:
                return pop2
            if pop1.left:
                Q1.append(pop1.left)
                Q2.append(pop2.left)
            if pop1.right:
                Q1.append(pop1.right)
                Q2.append(pop2.right)
