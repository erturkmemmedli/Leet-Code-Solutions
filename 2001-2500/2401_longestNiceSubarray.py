class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        result = 0
        window = 0
        start = 0

        for end, num in enumerate(nums):
            while window & num:
                window ^= nums[start]
                start += 1
            
            window |= num
            result = max(result, end - start + 1)
        
        return result
