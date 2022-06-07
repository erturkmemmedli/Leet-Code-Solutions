class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        for r, c in indices:
            for i in range(n):
                matrix[r][i] += 1
            for j in range(m):
                matrix[j][c] += 1
        count = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] % 2:
                    count += 1
        return count
