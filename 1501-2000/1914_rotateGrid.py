class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        i, j, r, c = 0, 0, len(grid) - 1, len(grid[0]) - 1
        while i < r and j < c:
            count = (r - i + c - j) * 2
            step = k % count
            indices = []
            for x in range(j, c + 1):
                indices.append((i, x, grid[i][x]))
            for y in range(i + 1, r + 1):
                indices.append((y, c, grid[y][c]))
            for x in range(c - 1, j - 1, -1):
                indices.append((r, x, grid[r][x]))
            for y in range(r - 1, i, -1):
                indices.append((y, j, grid[y][j]))
            for q in range(len(indices)):
                u, v, _ = indices[q]
                a, b, val = indices[(q + step) % len(indices)]
                grid[u][v] = val
            i, j, r, c = i + 1, j + 1, r - 1, c - 1
        return grid
