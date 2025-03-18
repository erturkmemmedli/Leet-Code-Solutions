class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 0
        AND = 0
        start = 0

        for end, num in enumerate(nums):
            while AND & num:
                AND ^= nums[start]
                start += 1
            
            AND |= num
            result = max(result, end - start + 1)
        
        return result
