class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        result = 0
        for row in grid:
            if row[0] == 0:
                for i in range(len(row)):   
                    if row[i] == 0: row[i] = 1
                    elif row[i] == 1: row[i] = 0
        result += len(grid) * 2 ** (len(grid[0]) - 1)
        for i, column in enumerate(zip(*grid)):
            count = column.count(0)
            if count > len(column)-count:
                result += count * 2 ** (len(grid[0]) - 1 - i)
            elif i:
                result += (len(column)-count) * 2 ** (len(grid[0]) - 1 - i)
        return result
