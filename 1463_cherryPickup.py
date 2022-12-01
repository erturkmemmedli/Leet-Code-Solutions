class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row, col1, col2):
            if row == m:
                return 0
            if col1 != col2:
                totalCherry = grid[row][col1] + grid[row][col2]
            else:
                totalCherry = grid[row][col1]
            answer = 0
            for c1 in range(col1-1, col1+2):
                for c2 in range(col2-1, col2+2):
                    if 0 <= c1 < n and 0 <= c2 < n:
                        answer = max(answer, dfs(row+1, c1, c2))
            return answer + totalCherry
            
        return dfs(0, 0, n-1)

# Alternative solution (which gives TLE error)

class Solution1:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.maxPickup = 0
        position1 = (0, 0)
        count1 = grid[0][0]
        position2 = (0, n-1)
        count2 = grid[0][n-1]
        self.dfs(grid, m, n, position1, position2, count1, count2)
        return self.maxPickup

    def dfs(self, grid, m, n, position1, position2, count1, count2):
        row1, col1 = position1
        row2, col2 = position2
        if row1 == m-1:
            self.maxPickup = max(self.maxPickup, count1 + count2)
            return
        for r1, c1 in [row1+1,col1-1], [row1+1,col1], [row1+1,col1+1]:
            for r2, c2 in [row2+1,col2-1], [row2+1,col2], [row2+1,col2+1]:
                if r1 < m and 0 <= c1 < n-1 and r2 < m and 0 < c2 < n and (r1, c1) != (r2, c2):
                    self.dfs(grid, m, n, (r1, c1), (r2, c2), count1 + grid[r1][c1], count2 + grid[r2][c2])
                    
# Alternative solution (which gives TLE error)

class Solution2:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n, self.maxPickup = len(grid), len(grid[0]), 0

        @lru_cache
        def dfs(row, col1, col2, count1, count2):
            if row == m-1:
                self.maxPickup = max(self.maxPickup, count1 + count2)
                return
            for c1 in (col1-1, col1, col1+1):
                for c2 in (col2-1, col2, col2+1):
                    if 0 <= c1 < n-1 and 0 < c2 < n and c1 < c2:
                        dfs(row+1, c1, c2, count1 + grid[row+1][c1], count2 + grid[row+1][c2])
            
        dfs(0, 0, n-1, grid[0][0], grid[0][n-1])
        return self.maxPickup
