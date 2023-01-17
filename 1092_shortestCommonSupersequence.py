class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n, = len(str1), len(str2)
        lcsMatrix = self.longestCommonSubsequence(str1, str2, m, n)
        self.firstStringCommonIndices, self.secondStringCommonIndices = [], []
        self.reconstructMatrix(lcsMatrix, str1, str2, m, n)
        shortestCommonSupersequence = self.buildSupersequence(str1, str2)
        return shortestCommonSupersequence

    def longestCommonSubsequence(self, str1, str2, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp

    def reconstructMatrix(self, mat, str1, str2, row, col):
        if row < 1 or col < 1:
            return
        if mat[row - 1][col] == mat[row][col - 1] == mat[row - 1][col - 1] == mat[row][col] - 1:
            self.reconstructMatrix(mat, str1, str2, row - 1, col - 1)
            self.firstStringCommonIndices.append(row - 1)
            self.secondStringCommonIndices.append(col - 1)
            return
        elif mat[row - 1][col] == mat[row][col]:
            return self.reconstructMatrix(mat, str1, str2, row - 1, col)
        elif mat[row][col - 1] == mat[row][col - 1]:
            return self.reconstructMatrix(mat, str1, str2, row, col - 1)

    def buildSupersequence(self, str1, str2):
        answer = ""
        first, second, current = 0, 0, 0
        while current < len(self.firstStringCommonIndices):
            f_curr = self.firstStringCommonIndices[current]
            s_curr = self.secondStringCommonIndices[current]
            if first < f_curr:
                answer += str1[first:f_curr]
                first = f_curr
            if second < s_curr:
                answer += str2[second:s_curr]
                second = s_curr
            if first == f_curr and second == s_curr:
                answer += str1[f_curr]
                current += 1
                first += 1
                second += 1
        answer += str1[first:]
        answer += str2[second:]
        return answer
