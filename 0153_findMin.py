class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.binary_search(nums, 0, len(nums) - 1)
        
    def binary_search(self, nums, left, right):
        mid = (left + right) // 2
        val = nums[mid]
        if left == right:
            return val
        if val >= nums[left] and nums[left] > nums[right]:
            return self.binary_search(nums, mid + 1, right)
        else:
            return self.binary_search(nums, left, mid)
