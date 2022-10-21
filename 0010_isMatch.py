class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matrix = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        matrix[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                matrix[0][i] = matrix[0][i-2]
        for i in range(1, len(s) + 1):
            matrix[i][0]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '.' or s[i-1] == p[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                elif j > 1 and p[j-1] == '*':
                    matrix[i][j] = matrix[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        matrix[i][j] = matrix[i][j] or matrix[i-1][j]
        return matrix[i][j]
