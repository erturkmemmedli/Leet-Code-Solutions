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

# Alternative solution

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]

        return a

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.rank[rb] > self.rank[ra]:
            self.parent[ra] = rb

        elif self.rank[rb] < self.rank[ra]:
            self.parent[rb] = ra

        else:
            self.rank[ra] += 1
            self.parent[rb] = ra
        
        return True

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)
        grid_val_map = {grid[i][j] : (i, j) for i in range(n) for j in range(n)}
        
        for i in range(n):
            for j in range(n):
                grid[i][j] = 0

        for i in range(n * n):
            r, c = grid_val_map[i]
            grid[r][c] = 1

            for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                if 0 <= row < n > col >= 0 and grid[row][col] == 1:
                    uf.union(r * n + c, row * n + col)

            if uf.find(0) == uf.find(n * n - 1):
                return i
