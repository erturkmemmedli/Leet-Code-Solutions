class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        summ = 0
        for num in nums:
            summ += num
            if summ < 0:
                result = max(result, summ)
                summ = 0
            else:
                result = max(result, summ)
        return result
