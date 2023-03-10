class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf')] * (i + 2) for i in range(1, len(triangle) + 1)]
        dp[0][1] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                dp[i][j + 1] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j + 1])
        return min(dp[-1])

# Alterntative solution

class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        base = triangle.pop()
        while triangle:
            new_base = triangle.pop()
            for i in range(len(new_base)):
                new_base[i] += min(base[i], base[i+1])
            base = new_base
        return base[0]
