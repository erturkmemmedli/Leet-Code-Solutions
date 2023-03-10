class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        summ, curMax, curMin, maxSum, minSum = 0, 0, 0, nums[0], nums[0]
        for num in nums:
            summ += num
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
        return max(maxSum, summ - minSum) if maxSum > 0 else maxSum
