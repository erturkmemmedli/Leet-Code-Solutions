class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        left = 0
        for i in range(len(nums)):
            left += nums[i]
            if summ == left:
                return i
            summ -= nums[i]
        return -1
