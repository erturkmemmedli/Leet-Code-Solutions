class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        queue = collections.deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j, 0))
        if len(queue) == n * n or len(queue) == 0:
            return -1
        while queue:
            row, col, dist = queue.popleft()
            visited.add((row, col))
            for r, c in [row-1, col], [row, col-1], [row+1, col], [row, col+1]:
                if 0 <= r < n > c >= 0 and (r, c) not in visited and grid[r][c] == 0:
                    queue.append((r, c, dist + 1))
                    visited.add((r, c))  
        return dist
