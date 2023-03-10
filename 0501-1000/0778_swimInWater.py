class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        leastTime = grid[0][0]
        heap = [(leastTime, 0, 0)]
        visited = {(0, 0)}
        while heap:
            time, r, c = heapq.heappop(heap)
            leastTime = max(leastTime, time)
            if r == n-1 and c == n-1:
                return leastTime
            for row, col in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if 0 <= row < n > col >= 0 and (row, col) not in visited:
                    heapq.heappush(heap, (grid[row][col], row, col))
                    visited.add((row, col))
