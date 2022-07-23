# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return -1
        minimum = float('inf')
        Q = deque([[root]])
        while Q:
            q = Q.popleft()
            for node in q:
                if node.val < minimum and node.val != root.val:
                    minimum = node.val
            level = []
            for node in q:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                Q.append(level)
        return minimum if minimum != float('inf') else -1
      
# Alternative solution

import heapq

class Solution1:
    def __init__(self):
        self.set = set()
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        L = list(self.set)
        heapq.heapify(L)
        heapq.heappop(L)
        try:
            return heapq.heappop(L)
        except:
            return -1
        
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.set.add(node.val)
        self.inorder(node.right)
        return node
