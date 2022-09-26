from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) not in visited:
                        queue = deque([(i, j)])
                        boundary = False
                        count = 0
                        while queue:
                            r, c = queue.popleft()
                            count += 1
                            visited.add((r, c))
                            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                                boundary = True
                            for row, col in (r-1,c), (r+1, c), (r,c-1), (r,c+1):
                                if 0 <= row < m and 0 <= col < n and (row, col) not in visited and grid[row][col] == 1:
                                    visited.add((row, col))
                                    queue.append((row, col))
                        if not boundary:
                            answer += count
        return answer
