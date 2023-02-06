class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[-1] = 0
        for i in range(n-2, -1, -1):
            j = nums[i]
            if not j: continue
            dp[i] = min(dp[i+1 : min(i+j+1, n)]) + 1
        return dp[0]
