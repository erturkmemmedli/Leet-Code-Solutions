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
