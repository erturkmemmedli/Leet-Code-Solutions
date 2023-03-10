class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        self.memo = {}
        return -1 if len(jobDifficulty) < d else self.dp(jobDifficulty, d, 0, 1)

    def dp(self, jobDifficulty, d, start, day):
        if (start, day) in self.memo: return self.memo[(start, day)]
        if d == day: return max(jobDifficulty[start:])
        result = float("inf")
        current = 0
        for i in range(start, len(jobDifficulty) - d + day):
            current = max(current, jobDifficulty[i])
            result = min(result, current + self.dp(jobDifficulty, d, i + 1, day + 1))
        self.memo[(start, day)] = result
        return self.memo[(start, day)]
