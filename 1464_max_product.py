class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = min(nums[0], nums[1])
        max2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if  max1 < nums[i] <= max2:
                max1 = nums[i]
            elif max2 < nums[i]:
                max1 = max2
                max2 = nums[i]
        return (max1-1) * (max2-1)
