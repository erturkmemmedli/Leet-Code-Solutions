class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(r, c, root):
            count = 0
            for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                if m > row >= 0 <= col < n:
                    if grid[row][col][0] == root and len(grid[row][col]) > 1:
                        count += 1
                    elif grid[row][col] == root:
                        grid[row][col] += '*'
                        if dfs(row, col, root):
                            return True
                    if count == 2:
                        return True

        for i in range(m):
            for j in range(n):
                if len(grid[i][j]) == 1:
                    root = grid[i][j]
                    grid[i][j] += '*'
                    if dfs(i, j, root):
                        return True
