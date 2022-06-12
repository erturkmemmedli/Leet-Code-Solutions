# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Q = deque([deque([root])])
        result = []
        while Q:
            node = Q.popleft()
            if not node: break
            else: Q.append(deque())
            nums = [] 
            while node:
                obj = node.popleft()
                nums.append(obj.val)
                if obj.left:
                    Q[0].append(obj.left)
                if obj.right:
                    Q[0].append(obj.right)
            result.append(sum(nums)/len(nums))
        return result
