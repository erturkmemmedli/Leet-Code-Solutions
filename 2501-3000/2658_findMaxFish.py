class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_fish_collected = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total = grid[i][j]
                    queue = deque([(i, j)])
                    grid[i][j] = 0

                    while queue:
                        r, c = queue.popleft()
                        for row, col in (r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c):
                            if m > row >= 0 <= col < n and grid[row][col] != 0:
                                queue.append((row, col))
                                total += grid[row][col]
                                grid[row][col] = 0
                            
                    max_fish_collected = max(max_fish_collected, total)
        
        return max_fish_collected
