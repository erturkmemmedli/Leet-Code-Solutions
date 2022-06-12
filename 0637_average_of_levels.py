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

# Alternative solution

class Solution1:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        storage = []
        depth = 0
        self.dfs(root, storage, depth)
        return [s/l for s, l in storage]
        
    def dfs(self, node, storage, depth):
        if node:
            if len(storage) <= depth:
                storage.append([0, 0])
            storage[depth][0] += node.val
            storage[depth][1] += 1
            self.dfs(node.left, storage, depth + 1)
            self.dfs(node.right, storage, depth + 1)

# Alternative solution

from collections import deque

class Solution2:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Q = deque([root])
        result = []
        while Q:
            n = len(Q)
            summ = 0
            for _ in range(n):
                node = Q.popleft()
                summ += node.val
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            result.append(summ/n)
        return result
