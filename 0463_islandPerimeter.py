class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    calc = 4
                    for r, c in [row-1,col], [row+1,col], [row,col-1], [row,col+1]:
                        if 0 <= r < m and 0 <= c < n and grid[r][c]:
                            calc -= 1
                    perimeter += calc
        return perimeter
