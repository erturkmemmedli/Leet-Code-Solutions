# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        return self.div_and_con(nums, left, right)
        
    def div_and_con(self, nums, left, right):
        if left > right:
            return
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.div_and_con(nums, left, mid - 1)
        node.right = self.div_and_con(nums, mid + 1, right)
        return node
