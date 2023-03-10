class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1: return n
        dp = [0, 1]
        mxm = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                x = dp[i//2]
                mxm = max(mxm, x)
                dp.append(x)
            else:
                x = dp[i//2] + dp[i//2 + 1]
                mxm = max(mxm, x)
                dp.append(x)
        return mxm
