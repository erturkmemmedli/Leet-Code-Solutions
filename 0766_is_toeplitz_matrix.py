class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n-2,-1,-1):
            cell = matrix[0][i]
            r = 0
            c = i
            while c < n and r < m:
                if cell != matrix[r][c]: return False
                r += 1
                c += 1
        for j in range(1, m-1):
            cell = matrix[j][0]
            r = j
            c = 0
            while r < m and c < n:
                if cell != matrix[r][c]: return False
                r += 1
                c += 1
        return True
