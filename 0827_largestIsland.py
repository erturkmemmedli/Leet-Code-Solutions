class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        islands = collections.defaultdict(int)
        candidates = collections.defaultdict(set)
        maxArea = 1
        # Breadth-First Search
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    # initiation of BFS parameters
                    queue = collections.deque([(i, j)])
                    visited.add((i, j))
                    area = 1
                    # detecting all the islands
                    while queue:
                        r, c = queue.popleft()
                        for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
                            if 0 <= row < n > col >= 0 and (row, col) not in visited:
                                # roaming into the island to determine its area
                                if grid[row][col] == 1:
                                    area += 1
                                    queue.append((row, col))
                                    visited.add((row, col))
                                # potential of non-island areas are determined
                                else:
                                    candidates[(row, col)].add((i, j))
                    maxArea = max(maxArea, area)
                    # each island's area is calculated
                    islands[(i, j)] = area
        # Finding potential non-island area to make largest island
        for key, candidate in candidates.items():
            area = 1
            for row, col in candidate:
                area += islands[(row, col)]
            maxArea = max(maxArea, area)
        return maxArea

# Alternative solution (which gives TLE error)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        islands = []
        maxArea = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    queue = collections.deque([(i, j)])
                    visited.add((i, j))
                    neighbors = set()
                    area = 1
                    while queue:
                        r, c = queue.popleft()
                        for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
                            if 0 <= row < n > col >= 0 and (row, col) not in visited:
                                if grid[row][col] == 1:
                                    area += 1
                                    queue.append((row, col))
                                    visited.add((row, col))
                                else:
                                    neighbors.add((row, col))
                    maxArea = max(maxArea, area)
                    islands.append((area, neighbors))
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    possibleArea = 1
                    for k in range(len(islands)):
                        area, neighbors = islands[k]
                        max
                        if (i, j) in neighbors:
                            possibleArea += area
                    maxArea = max(maxArea, possibleArea)
        return maxArea
