from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        Q = deque()
        distance = [[float('inf') if grid[r][c] == 1 else 0 for c in range(n)] for r in range(m)] 
        visited = set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2: Q.append((row, col))
        while Q:
            row, col = Q.popleft()
            if (row, col) not in visited:
                visited.add((row, col))
                for i, j in (row-1,col), (row+1,col), (row,col-1), (row,col+1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        Q.append((i, j))
                        distance[i][j] = min(distance[i][j], distance[row][col]+1)
        minute = max([distance[r][c] for r in range(m) for c in range(n)])
        return -1 if minute == float('inf') else minute
