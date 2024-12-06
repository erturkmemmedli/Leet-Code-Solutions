# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.total = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            summ = node.val + left_sum + right_sum
            count = 1 + left_count + right_count

            avg = summ // count
            self.total += (avg == node.val)
            return summ, count
        
        dfs(root)
        return self.total
