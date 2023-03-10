class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        path_sum = 0
        for row in range(1, n):
            for col in range(n):
                summ = float('inf')
                for r, c in (row - 1, col - 1), (row - 1, col), (row - 1, col + 1):
                    if 0 <= r < n > c >= 0:
                        summ = min(summ, matrix[row][col] + matrix[r][c])
                matrix[row][col] = summ
        return min(matrix[-1])
