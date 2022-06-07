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

# Alternative solution

class Solution1:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        for r, c in indices:
            row[r] += 1
            col[c] += 1
        count = 0
        for i in row:
            for j in col:
                if (i+j) % 2:
                    count += 1
        return count
