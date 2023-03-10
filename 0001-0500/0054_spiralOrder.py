class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 0, 1
        spiral = []
        while len(spiral) < m * n:
            spiral.append(matrix[x][y])
            matrix[x][y] = None
            if 0 <= x + dx < m and 0 <= y + dy < n and matrix[x + dx][y + dy] != None:
                x += dx
                y += dy
            else:
                dx, dy = dy, -dx
                x += dx
                y += dy
        return spiral
