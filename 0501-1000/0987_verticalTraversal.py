# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.heap = []
        self.dfs(root, 0, 0)
        answer, lastColumn = [], None
        while self.heap:
            col, row, val = heapq.heappop(self.heap)
            if col != lastColumn:
                answer.append([val])
                lastColumn = col
            else:
                answer[-1].append(val)
        return answer

    def dfs(self, node, row, col):
        if not node: return
        heapq.heappush(self.heap, (col, row, node.val))
        self.dfs(node.left, row + 1, col - 1)
        self.dfs(node.right, row + 1, col + 1)
