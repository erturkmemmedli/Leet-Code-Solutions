class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)
        max_val = 0
        for i in range(k):
            max_val = max(max_val, arr[i])
            dp[i] = max_val * (i+1)
        for i in range(k, len(arr)):
            x = i-k+1
            value = 0
            while x <= i:
                max_val = max(arr[x:i+1])
                value = max(value, dp[x-1] + max_val * (i-x+1))
                x += 1
            dp[i] = value
        return dp[-1]
