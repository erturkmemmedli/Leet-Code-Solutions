class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        grid_set = set(range(1, n ** 2 + 1))
        a = None

        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if val not in grid_set:
                    a = val
                else:
                    grid_set.remove(val)
                
        return [a, grid_set.pop()]
