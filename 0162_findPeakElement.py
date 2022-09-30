class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binary_search(nums, 0, len(nums)-1)
        
    def binary_search(self, nums, left, right):
        if left == right:
            return left
        mid = (left + right) // 2
        if mid != 0 and mid != len(nums)-1 and nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        elif mid == 0 and nums[mid+1] < nums[mid]:
            return mid
        elif mid == len(nums)-1 and nums[mid-1] < nums[mid]:
            return mid
        l = self.binary_search(nums, mid+1, right)
        r = self.binary_search(nums, left, mid)
        return l if nums[l] > nums[r] else r
