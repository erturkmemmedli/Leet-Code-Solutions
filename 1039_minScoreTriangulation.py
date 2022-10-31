class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        self.memoization = {}
        return self.dp(values, 0, len(values) - 1)

    def dp(self, v, i, j):
        if (i, j) not in self.memoization:
            self.memoization[(i, j)] = min([v[i] * v[j] * v[k] + self.dp(v, i, k) + self.dp(v, k, j) for k in range(i + 1, j)] or [0])
        return self.memoization[(i, j)]

# ALterntive solution (which gives TLE error)

class Solution1:
    def minScoreTriangulation(self, values: List[int]) -> int:
        self.min = math.inf
        return self.dp(values)

    def dp(self, w):
        if len(w) == 3:
            return w[0] * w[1] * w[2]
        for j in range(len(w)):
            if j == 0:
                self.min = min(self.min, w[-1] * w[j] * w[j+1] + self.dp(w[j+1:]))
            elif j == len(w) - 1:
                self.min = min(self.min, w[j-1] * w[j] * w[0] + self.dp(w[:j]))
            else:
                self.min = min(self.min, w[j-1] * w[j] * w[j+1] + self.dp(w[:j] + w[j+1:]))
        return self.min
