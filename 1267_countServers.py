from collections import deque, defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        can_communicate = 0
        visited, rows, cols = set(), defaultdict(int), defaultdict(int)
        single_servers = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if (i, j) not in visited:
                        visited.add((i, j))
                        rows[i], cols[j] = rows[i] + 1, cols[j] + 1
                        queue = deque([(i, j)])
                        number_of_servers = 1
                        while queue:
                            r, c = queue.popleft()
                            for row, col in [r-1,c], [r+1,c], [r,c-1], [r,c+1]:
                                if 0 <= row < m and 0 <= col < n and grid[row][col] and (row, col) not in visited:
                                    number_of_servers += 1
                                    queue.append((row, col))
                                    visited.add((row, col))
                                    rows[row], cols[col] = rows[row] + 1, cols[col] + 1
                        if number_of_servers > 1:
                            can_communicate += number_of_servers
                            number_of_servers = 1
                        else:
                            single_servers.append((i, j))
        for row, col in single_servers:
            if rows[row] > 1 or cols[col] > 1:
                can_communicate += 1
        return can_communicate
