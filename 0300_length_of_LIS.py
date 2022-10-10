from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            index = bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
        return len(dp)

# Alternative solution

class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        array = [0] * (n + 1)
        array[1] = 1
        for i in range(2, n + 1):
            maximum = - float('inf')
            for j in range(i-1, 0, -1):
                if nums[i-1] > nums[j-1]:
                    array[i] = array[j] + 1
                else:
                    array[i] = 1
                maximum = max(array[i], maximum)
            array[i] = maximum
        return max(array)

# Alternative solution

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums) + 1)
        for i in range(2, len(nums) + 1):
            for j in range(i-1, 0, -1):
                if nums[i-1] > nums[j-1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
