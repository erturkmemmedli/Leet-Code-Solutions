class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxSquareSize = 0

        def findUpAndLeft(i, j):
            a, b = i, j
            while a - 1 >= 0 and b - 1 >= 0 and grid[a - 1][j] == 1 and grid[i][b - 1]:
                a, b = a - 1, b - 1
            return a, b

        def calculate(i, j, x, y):
            if i == x and j == y:
                return 1
            if grid[x][y] == 0:
                return calculate(i, j, x + 1, y + 1)
            else:
                if checkBottomAndRight(i, j, x, y):
                    return (i - x + 1) ** 2
                else:
                    return calculate(i, j, x + 1, y + 1)

        def checkBottomAndRight(i, j, x, y):
            a, b = x, y
            while a < i and b < j:
                if grid[a + 1][y] == 1 and grid[x][b + 1] == 1:
                    a, b = a + 1, b + 1
                else:
                    return False
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = findUpAndLeft(i, j)
                    maxSquareSize = max(maxSquareSize, calculate(i, j, x, y))
        
        return maxSquareSize
