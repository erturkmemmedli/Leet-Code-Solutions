# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from heapq import heappush, heappop
from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        heap = []

        while queue:
            length = len(queue)
            level_sum = 0

            for _ in range(length):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if len(heap) < k:
                heappush(heap, level_sum)
            elif heap[0] < level_sum:
                heappop(heap)
                heappush(heap, level_sum)
            
        return heap[0] if len(heap) == k else -1
