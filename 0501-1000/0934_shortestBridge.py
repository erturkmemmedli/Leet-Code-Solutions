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

# Alternative solution

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        island_found = False
        borders = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    queue = deque([(i, j)])

                    while queue:
                        r, c = queue.popleft()

                        for row, col in (r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1):
                            if m > row >= 0 <= col < n and grid[row][col] == 0:
                                heappush(borders, (0, r, c))
                                break

                        for row, col in (r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1):
                            if m > row >= 0 <= col < n and grid[row][col] == 1:
                                queue.append((row, col))
                                grid[row][col] = -1
                    
                    island_found = True
                    break
            
            if island_found:
                break

        while borders:
            distance, r, c = heappop(borders)

            for row, col in (r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1):
                if m > row >= 0 <= col < n:
                    if grid[row][col] == 0:
                        grid[row][col] = -1
                        heappush(borders, (distance + 1, row, col))
                    if grid[row][col] == 1:
                        return distance

# Alternative solution

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        firstIsland = set()
        secondIsland = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in firstIsland and (i, j) not in secondIsland:
                    # POLYMORPHISM fir island sets
                    island = firstIsland if not firstIsland else secondIsland
                    queue = deque([(i, j)])
                    island.add((i, j))

                    while queue:
                        r, c = queue.popleft()

                        for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                            if n > row >= 0 <= col < n and grid[row][col] == 1 and (row, col) not in island:
                                queue.append((row, col))
                                island.add((row, col))
                elif grid[i][j] == 0:
                    grid[i][j] = float('inf')

        heap = []
        
        for i, j in firstIsland:
            heappush(heap, (0, i, j))
        
        while heap:
            dist, r, c = heappop(heap)

            for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                if n > row >= 0 <= col < n and (row, col) not in firstIsland:
                    if (row, col) in secondIsland:
                        return dist
                    if grid[row][col] > dist + 1:
                        firstIsland.add((row, col))
                        heappush(heap, (dist + 1, row, col))
        
