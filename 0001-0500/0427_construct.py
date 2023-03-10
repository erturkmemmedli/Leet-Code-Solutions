"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from random import randint

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], 1)
        root = Node()
        if n == 2:
            if grid[0][0] == grid[0][1] == grid[1][0] == grid[1][1]:
                root.isLeaf = 1
                root.val = grid[0][0]
            else:
                root.isLeaf = 0
                root.val = randint(0,1)
                root.topLeft = Node(grid[0][0], 1)
                root.topRight = Node(grid[0][1], 1)
                root.bottomLeft = Node(grid[1][0], 1)
                root.bottomRight = Node(grid[1][1], 1)
            return root
        if n > 2:            
            root.topLeft = self.construct([i[:n//2] for i in grid[:n//2]])
            root.topRight = self.construct([i[n//2:] for i in grid[:n//2]])
            root.bottomLeft = self.construct([i[:n//2] for i in grid[n//2:]])
            root.bottomRight = self.construct([i[n//2:] for i in grid[n//2:]])
            if root.topLeft.isLeaf and root.topRight.isLeaf and root.bottomLeft.isLeaf and root.bottomRight.isLeaf:
                if root.topLeft.val == root.topRight.val == root.bottomLeft.val == root.bottomRight.val:
                    root.isLeaf = 1
                    root.val = root.topLeft.val
                    root.topLeft, root.topRight, root.bottomLeft, root.bottomRight = None, None, None, None
                else:
                    root.isLeaf = 0
                    root.val = randint(0,1)
            else:
                root.isLeaf = 0
                root.val = randint(0,1)
        return root
