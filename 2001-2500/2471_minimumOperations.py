# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        number_of_operations = 0

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)
                
            val_idx = {v:k for k, v in enumerate(sorted(level))}
            i = 0

            while i < len(level):
                val = level[i]
                if i == val_idx[val]:
                    i += 1
                else:
                    idx = val_idx[val]
                    level[i], level[idx] = level[idx], level[i]
                    number_of_operations += 1
                
        return number_of_operations
