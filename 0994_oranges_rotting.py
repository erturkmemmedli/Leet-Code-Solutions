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

# Alternative solution

from collections import deque

class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        Queue = deque()
        orangeCount = 0
        minute = 0
        rottenOranges = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1:
                    orangeCount += 1
                if grid[i][j] == 2:
                    orangeCount += 1
                    rottenOranges.append((i,j))
        Queue.append(rottenOranges)
        while Queue:
            rotten = Queue.popleft()
            new_rotten_oranges = []
            for r, c in rotten:
                if (r, c) not in visited:
                    visited.add((r, c))
                    for row, col in [r-1,c], [r+1,c], [r,c-1], [r,c+1]:
                        if 0 <= row < m and 0 <= col < n and grid[row][col] == 1 and (row, col) not in visited:
                            grid[row][col] = 2
                            new_rotten_oranges.append((row,col))
            if new_rotten_oranges:
                Queue.append(new_rotten_oranges)
                minute += 1
        return minute if len(visited) == orangeCount else -1
