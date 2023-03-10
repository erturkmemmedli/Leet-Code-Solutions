class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.total = 0
        start_position, end_position, obstacle_count = None, None, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    obstacle_count += 1
                elif grid[i][j] == 1:
                    start_position = (i, j)
                elif grid[i][j] == 2:
                    end_position = (i, j)
        total_path = m * n - obstacle_count
        visited = set()
        self.dfs(start_position, end_position, total_path, visited, grid, m, n)
        return self.total
        
    def dfs(self, start, end, total, visited, grid, m, n):
        if start == end:
            if len(visited) == total - 1:
                self.total += 1
            return
        a, b = start
        if start not in visited:
            visited.add(start)
            for row, col in [a-1, b], [a+1, b], [a, b-1], [a, b+1]:
                if 0 <= row < m and 0 <= col < n and grid[row][col] not in visited and grid[row][col] != -1:
                    self.dfs((row,col), end, total, visited, grid, m, n)
            visited.discard(start)
