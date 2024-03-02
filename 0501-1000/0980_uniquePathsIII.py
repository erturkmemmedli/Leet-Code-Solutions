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

# Alternative solution

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = col = None
        obs = 0

        for i in range(m):
            for j in range(n):                
                if grid[i][j] == 1:
                    row, col = i, j 
                if grid[i][j] == -1:
                    obs += 1

        self.result = 0
        self.dfs(grid, m, n, row, col, obs)
        return self.result

    def dfs(self, grid, m, n, i, j, count):
        if grid[i][j] == 2:
            if count == m * n - 1:
                self.result += 1
            return

        temp = grid[i][j]
        grid[i][j] = -1

        for row, col in (i-1, j), (i, j-1), (i+1, j), (i, j+1):
            if m > row >= 0 <= col < n and grid[row][col] != -1:
                self.dfs(grid, m, n, row, col, count + 1)

        grid[i][j] = temp

# Alternative solution

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        src = None
        mask = 0
        memo = {}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    src = (i, j)
                if grid[i][j] in [-1, 1]:
                    mask ^= 1 << (i * n + j)
                
        def dp(r, c, mask):
            if mask == (1 << m * n) - 1 and grid[r][c] == 2:
                return 1

            if (r, c, mask) in memo:
                return memo[(r, c, mask)]

            memo[(r, c, mask)] = 0

            for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                if m > row >= 0 <= col < n and grid[row][col] != -1:
                    new_mask = mask ^ (1 << (row * n + col))
                    if not mask & (1 << (row * n + col)):
                        memo[(r, c, mask)] += dp(row, col, new_mask)

            return memo[(r, c, mask)]

        return dp(src[0], src[1], mask)
