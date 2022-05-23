class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.binary_search(nums, target, left, right)
    
    def binary_search(self, nums, target, left, right):
        mid = (left + right) // 2
        if left > right:
            return -1
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binary_search(nums, target, left, mid - 1)
        if nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, right)
