class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        summ = 0
        result = 0
        for i in range(len(nums)):
            summ += nums[i]
            result = max(result, (summ + i) // (i + 1))
        return result
