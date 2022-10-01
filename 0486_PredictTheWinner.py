class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[None] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = (nums[i], 0)
        for i in range(1, len(nums)):
            step = len(nums) - i
            for j in range(step):
                left = (dp[j][i+j-1][1] + nums[i+j], dp[j][i+j-1][0])
                bottom = (dp[j+1][i+j][1] + nums[j], dp[j+1][i+j][0])
                dp[j][i+j] = max(left, bottom, key = lambda x: x[0])
        return dp[0][-1][0] >= dp[0][-1][1]
