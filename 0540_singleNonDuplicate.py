class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        mid = (len(nums) - 1) // 2
        if len(nums) == 1: return nums[mid]
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]: return nums[mid]
        if mid % 2:
            if nums[mid] == nums[mid-1]:
                return self.singleNonDuplicate(nums[mid+1:])
            else:
                return self.singleNonDuplicate(nums[:mid])
        else:
            if nums[mid] == nums[mid+1]:
                return self.singleNonDuplicate(nums[mid+2:])
            else:
                return self.singleNonDuplicate(nums[:mid-1])
