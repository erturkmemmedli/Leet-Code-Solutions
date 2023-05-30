class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(min(zero, one), high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]

        total = 0

        for i in range(low, high + 1):
            total += dp[i]

        return total % 1_000_000_007
      
# Alternative solution (which gives TLE error)

from math import comb

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [[0] * high  for _ in range(high)]

        for i in range(high):
            dp[i][i] = self.combination(i + 1, zero, one)

        for k in range(high):
            for i in range(high - k - 1):
                j = i + k + 1

                if j == high:
                    break

                dp[i][j] = dp[i][i] + dp[i + 1][j] 

        return dp[low-1][high-1] % 1_000_000_007
            
    def combination(self, num, zero, one):
        count = 0
        i = num // zero
        while i >= 0:
            zeros = i * zero
            ones = num - zeros
            if ones % one == 0:
                j = ones // one
                total = i + j
                count += comb(total, i)
            i -= 1
        return count

# Alternative solution (which gives MLE error)

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.memo = {}
        return self.dp(low, high, zero, one, "")

    def dp(self, low, high, zero, one, path):
        if len(path) > high:
            return 0

        if len(path) == high:
            return 1

        if path in self.memo:
            return self.memo[path]

        result = self.dp(low, high, zero, one, path + '0' * zero) + self.dp(low, high, zero, one, path + '1' * one)

        if len(path) >= low:
            result += 1
            
        self.memo[path] = result
        return self.memo[path]
        
