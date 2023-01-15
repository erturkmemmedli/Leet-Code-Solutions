class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                result = max(result, count)
            else:
                count = 0
        return result

# Alternative solution

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = -1
        maxOnes = 0
        for right, num in enumerate(nums):
            if num == 1:
                maxOnes = max(maxOnes, right - left)
            else:
                left = right
        return maxOnes
