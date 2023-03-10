class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        numIslands = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    self.included = True
                    self.visitIsland(grid1, grid2, m, n, i, j)
                    if self.included:
                        numIslands += 1
        return numIslands

    def visitIsland(self, grid1, grid2, m, n, row, col):
        if m > row >= 0 <= col < n and grid2[row][col]:
            if grid1[row][col] == 0:
                self.included = False
            grid2[row][col] = 0
            self.visitIsland(grid1, grid2, m, n, row - 1, col)
            self.visitIsland(grid1, grid2, m, n, row + 1, col)
            self.visitIsland(grid1, grid2, m, n, row, col - 1)
            self.visitIsland(grid1, grid2, m, n, row, col + 1)
