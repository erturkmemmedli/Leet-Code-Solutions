class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            for row in grid:
                for i in range(len(row)-1,0,-1):
                    row[i], row[i-1] = row[i-1], row[i]
            for j in range(len(grid)-1,0,-1):
                grid[j][0], grid[j-1][0] = grid[j-1][0], grid[j][0]
        return grid
      
# Alternative solution

class Solution1:
    def shiftGrid(self, grid, k: int):
        m = len(grid)
        n = len(grid[0])
        l = m * n
        k = k % l
        combined = [x for row in grid for x in row]
        combined = combined[l-k:] + combined[:l-k]
        print(combined)
        result = []
        for i in range(0, m*n, n):
            result.append(combined[i:i+n])
        return result

# Alternative solution

class Solution2:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k // len(grid[0])):
            grid.insert(0, grid.pop())
        k = k % len(grid[0])
        for _ in range(k):
            for row in grid:
                for i in range(len(row)-1,0,-1):
                    row[i], row[i-1] = row[i-1], row[i]
            for j in range(len(grid)-1,0,-1):
                grid[j][0], grid[j-1][0] = grid[j-1][0], grid[j][0]
        return grid
