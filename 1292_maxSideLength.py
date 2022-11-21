class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # construction of prefix sum matrix
        mat = [[0] * len(mat[0])] + mat
        for i in range(len(mat)):
            mat[i] = [0] + mat[i]
        m, n = len(mat), len(mat[0])
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] += mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
        # diagonal traverse for maximum sum square
        sideLength = 0
        for i in range(1, m):
            for j in range(1, n):
                u, v = i - 1, j - 1
                while u >= 0 and v >= 0:
                    if mat[i][j] - mat[u][j] - mat[i][v] + mat[u][v] <= threshold:
                        sideLength = max(sideLength, i - u)
                        u, v = u - 1, v - 1
                    else:
                        break
        return sideLength
