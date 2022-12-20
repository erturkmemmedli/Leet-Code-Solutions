from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        distance = [[float('inf') for _ in range(n)] for _ in range(n)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        distance[0][0] = 1
        Q = deque([(0, 0)])
        while Q:
            i, j = Q.popleft()
            if not visited[i][j]:
                visited[i][j] = True
                for ix, jx in (i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1):
                    if ix >= 0 and jx >= 0 and ix < n and jx < n and grid[ix][jx] == 0:
                        if not visited[ix][jx]:
                            Q.append((ix, jx))
                        distance[ix][jx] = min(distance[ix][jx], distance[i][j] + 1)
        return distance[-1][-1] if distance[-1][-1] != float('inf') else -1

# Alternative solution

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        n = len(grid)
        heap = [(1, 0, 0)]
        visited = {(0, 0)}
        while heap:
            distance, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return distance
            for row, col in [r-1,c-1],[r-1,c],[r-1,c+1],[r,c-1],[r,c+1],[r+1,c-1],[r+1,c],[r+1,c+1]:
                if 0 <= row < n > col >= 0 and (row, col) not in visited and grid[row][col] == 0:
                    heapq.heappush(heap, (distance + 1, row, col))
                    visited.add((row, col))
        return -1
