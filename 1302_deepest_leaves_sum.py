# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        result = 0
        temp = 0
        Q = deque([deque([root])])
        while Q:
            if len(Q) == 1:
                Q.append(deque([]))
            if not len(Q[0]):
                return result
            node = Q[0].popleft()
            if temp == 0:
                temp = node.val
                result = temp
            if len(Q[0]):
                temp += Q[0][0].val
                result = temp
            else:
                Q.popleft()
                temp = 0
            if node.left:
                Q[-1].append(node.left)
            if node.right:
                Q[-1].append(node.right)

# Alternative solution

from collections import deque

class Solution1:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        Q = deque([[root]])
        while Q:
            level = Q.popleft()
            pack = []
            for node in level:
                if node.left:
                    pack.append(node.left)
                if node.right:
                    pack.append(node.right)
            if pack: Q.append(pack)
        return sum([node.val for node in level])
