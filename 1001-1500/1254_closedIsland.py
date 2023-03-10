class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        closed_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if (i, j) not in visited:
                        visited.add((i, j))
                        queue = collections.deque([(i, j)])
                        in_boundary = False
                        while queue:
                            r, c = queue.popleft()
                            if r == 0 or r == m-1 or c == 0 or c == n-1:
                                in_boundary = True
                            visited.add((r, c))
                            for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
                                if 0 <= row < m and 0 <= col < n and grid[row][col] == 0 and (row, col) not in visited:
                                    if row == 0 or row == m-1 or col == 0 or col == n-1:
                                        in_boundary = True
                                    queue.append((row, col))
                                    visited.add((row, col))
                        if not in_boundary:
                            closed_islands += 1
        return closed_islands
