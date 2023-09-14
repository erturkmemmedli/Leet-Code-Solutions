class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        zeroCount = 0
        maxLength = 0
        for right, num in enumerate(nums):
            if num != 1:
                zeroCount += 1
                while zeroCount > 1:
                    if nums[left] == 0:
                        zeroCount -= 1
                    left += 1
            maxLength = max(maxLength, right - left + 1)    
        return maxLength
