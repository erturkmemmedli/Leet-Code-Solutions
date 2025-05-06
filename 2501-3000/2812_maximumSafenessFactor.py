class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
            
        dist = [[inf] * n for _ in range(n)]
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                if 0 <= row < n > col >= 0 and dist[row][col] == inf:
                    dist[row][col] = dist[r][c] + 1
                    queue.append((row, col))

        left, right = 0, n * 2
        while left < right:
            mid = (left + right + 1) // 2
            if self.can_reach_end(dist, mid):
                left = mid
            else:
                right = mid - 1
                
        return left

    def can_reach_end(self, dist, min_dist):
        n = len(dist)
        if dist[0][0] < min_dist or dist[n-1][n-1] < min_dist:
            return False
            
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            if r == n - 1 and c == n - 1:
                return True
                
            for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= row < n > col >= 0 and (row, col) not in visited and dist[row][col] >= min_dist:
                    visited.add((row, col))
                    queue.append((row, col))
        
        return False 
