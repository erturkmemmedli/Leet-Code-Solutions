class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        mod = 10 ** 9 + 7

        # suffix sum
        suffix_sum = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                suffix_sum[i][j] = (
                    (1 if pizza[i][j] == 'A' else 0) +
                    (suffix_sum[i + 1][j] if i + 1 < m else 0) +
                    (suffix_sum[i][j + 1] if j + 1 < n else 0) -
                    (suffix_sum[i + 1][j + 1] if (i + 1) < m and (j + 1) < n else 0)
                )

        # dynamic programming with memoization
        memo = {}

        def dp(x, y, cut):
            if cut == 0:
                memo[(x, y, cut)] = 1
                return memo[(x, y, cut)]

            if (x, y, cut) in memo:
                return memo[(x, y, cut)]

            count = 0

            # horizaontal cut
            for i in range(x, m - 1):
                if suffix_sum[i + 1][y] != 0 and (suffix_sum[x][y] - suffix_sum[i + 1][y] != 0):
                    count += dp(i + 1, y, cut - 1)

            # vertical cut
            for j in range(y, n - 1):
                if suffix_sum[x][j + 1] != 0 and (suffix_sum[x][y] - suffix_sum[x][j + 1] != 0):
                    count += dp(x, j + 1, cut - 1)

            memo[(x, y, cut)] = count % mod
            return memo[(x, y, cut)]

        return dp(0, 0, k - 1)
