class Solution:
    def numTilings(self, n: int) -> int:
        dp = collections.deque([[1,1],[2,2]])
        if n < 3: return dp[n-1][0]
        for _ in range(n-2):
            first = dp[0][0] + dp[1][0] + 2 * dp[0][1]
            second = dp[1][0] + dp[1][1]
            dp.popleft()
            dp.append([first, second])
        return dp[-1][0] % (10**9 + 7)

# Alternative solution

class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3: return n
        a, b, c = 1, 1, 2
        for _ in range(n - 2):
            a, b, c, = b, c, 2 * c + a
        return c % 1000000007
