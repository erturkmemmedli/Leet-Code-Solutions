class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row = 0
        col = n - 1
        count = 0
        while row < m and col >= 0:
            if grid[row][col] < 0:
                if col - 1 >= 0 and grid[row][col-1] < 0:
                    col -= 1
                    continue
                else:
                    count += n - col
                    row += 1
            else:
                row += 1
        return count
