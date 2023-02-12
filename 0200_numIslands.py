from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        number_of_islands = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if (i, j) not in visited:
                        queue = deque([(i, j)])
                        visited.add((i, j))
                        while queue:
                            r, c = queue.popleft()
                            for row, col in [r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]:
                                if 0 <= row < m and 0 <= col < n and grid[row][col] == '1' and (row, col) not in visited:
                                    queue.append((row, col))
                                    visited.add((row, col))
                        number_of_islands += 1
        return number_of_islands
        
# Alternative solution

class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        number_of_islands = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if (i, j) not in visited:
                        self.dfs(grid, visited, i, j, m, n)
                        number_of_islands += 1
        return number_of_islands
    
    def dfs(self, grid, visited, i, j, m, n):
        if (i, j) not in visited:
            visited.add((i, j))
            for row, col in [i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]:
                if 0 <= row < m and 0 <= col < n and grid[row][col] == '1' and (row, col) not in visited:
                    self.dfs(grid, visited, row, col, m, n)

# Alternative solution

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        numOfIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    self.traverseIsland(grid, m, n, i, j)
        return numOfIslands

    def traverseIsland(self, matrix, m, n, row, col):
        if m > row >= 0 <= col < n and matrix[row][col] == '1':
            matrix[row][col] = '0'
            self.traverseIsland(matrix, m, n, row, col + 1)
            self.traverseIsland(matrix, m, n, row + 1, col)
            self.traverseIsland(matrix, m, n, row, col - 1)
            self.traverseIsland(matrix, m, n, row - 1, col)
