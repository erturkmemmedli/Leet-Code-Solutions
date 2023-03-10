class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    dp[i] += 1
        return dp
      
# Alternative solution

class Solution1:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse = True)
        dictionary = {sorted_nums[-1] : 0}
        for i in range(len(nums)-1):
            if sorted_nums[i] > sorted_nums[i+1]:
                dictionary[sorted_nums[i]] = len(nums) - i - 1
        result = []
        for num in nums:
            result.append(dictionary[num])
        return result
