# class Algorithm:
#     def findMaximumElement(self, arr):
#         maximumValue, maximumIndex, searchCost, n = -1, -1, 0, len(arr)
#         for i in range(n):
#             if maximumValue < arr[i]:
#                 maximumValue, maximumIndex, searchCost = arr[i], i, searchCost + 1
#                 # where searchCost is k.
#         return maximumIndex

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # k = 1 means reverse sorted array
        # k - 1 times increase, i.e arr[i] > arr[i-1]
        # if k > m, it is impossible
        if k > m: return 0
        dp = [[[0] * (m+1) for _ in range(k+1)] for _ in range(n+1)]
        for M in range(1, m+1):
            dp[1][1][M] = 1
        for N in range(1, n+1):
            for K in range(1, k+1):
                for M in range(m+1):
                    dp[N][K][M] += dp[N-1][K][M] * M
                    dp[N][K][M] += sum(dp[N-1][K-1][1:M])
        return sum(dp[n][k][1:]) % (10**9 + 7)
        
# Alternative solution

class Solution1:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.mod = 1000000007
        return sum(self.dp(n, i, k) for i in range(1, m+1)) % self.mod

    @functools.lru_cache(None)
    def dp(self, arrayLength, largestNumber, searchCost):
        if arrayLength == 1:
            return 1 if searchCost == 1 else 0
        if searchCost == 0:
            return 0
        # no searchcost on last number
        result = self.dp(arrayLength - 1, largestNumber, searchCost) * largestNumber
        # searchcost on last number
        result += sum(self.dp(arrayLength - 1, i, searchCost - 1) for i in range(1, largestNumber))
        return result % self.mod
