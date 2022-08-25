class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] != s2[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
        lcs_sum = dp[-1][-1]
        total_sum = sum(ord(i) for i in s1 + s2)
        return total_sum - 2 * lcs_sum

# Alternative solution. Time Limit Exceeded (TLE) error. Backtracking part needs to be fixed.

class Solution1:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                left = dp[i][j-1]
                top = dp[i-1][j]
                diag = dp[i-1][j-1]
                match = dp[i-1][j-1] + 1
                if s1[i-1] == s2[j-1] and left == top == diag:
                    dp[i][j] = max(left, top, match)
                else:
                    dp[i][j] = max(left, top, diag)
        combinations, characters, memoization = [], [], set()
        self.backtrack(s1, s2, dp, memoization, combinations, characters, m, n)
        lcs_sum = max([sum([ord(i) for i in ch]) for ch in combinations])
        total_sum = sum(ord(i) for i in s1 + s2)
        return total_sum - 2 * lcs_sum

    def backtrack(self, s1, s2, matrix, memo, comb, char, i, j):
        if (i, j) not in memo:
            memo.add((i,j))
            if i == 0 and j == 0:
                comb.append(char)
                return
            if len(char) == matrix[-1][-1]:
                comb.append(char)
                return
            if i > 0 and matrix[i][j] == matrix[i-1][j]:
                self.backtrack(s1, s2, matrix, memo, comb, char, i-1, j)
            if j > 0 and matrix[i][j] == matrix[i][j-1]:
                self.backtrack(s1, s2, matrix, memo, comb, char, i, j-1)
            if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1]:
                self.backtrack(s1, s2, matrix, memo, comb, char, i-1, j-1)
            elif i > 0 and j > 0 and s1[i-1] == s2[j-1]:
                self.backtrack(s1, s2, matrix, memo - {(i,j)}, comb, char + [s1[i-1]], i-1, j-1)
        return
