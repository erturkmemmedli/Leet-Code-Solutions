class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        firstIslandBorders = set()
        secondIslandBorders = set()
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) not in visited:
                        # BFS to find border points of each island
                        queue = collections.deque([(i, j)])
                        visited.add((i, j))
                        borders = set()
                        while queue:
                            r, c = queue.popleft()
                            for row, col in (r, c-1), (r, c+1), (r-1, c), (r+1, c):
                                if 0 <= row < n > col >= 0:
                                    if grid[row][col] == 0:
                                        borders.add((r, c))
                                    else:
                                        if (row, col) not in visited:
                                            visited.add((row, col))
                                            queue.append((row, col))
                        if not firstIslandBorders:
                            firstIslandBorders = borders
                        else:
                            secondIslandBorders = borders
        # Find the shortest path between the border coordinates
        shortestPath = math.inf
        for r1, c1 in firstIslandBorders:
            for r2, c2 in secondIslandBorders:
                shortestPath = min(shortestPath, abs(r1 - r2) + abs(c1 - c2) - 1)
        return shortestPath
