class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        '''
        1 -> right --- from grid[i][j] to grid[i][j + 1]
        2 -> left  --- from grid[i][j] to grid[i][j - 1]
        3 -> down  --- from grid[i][j] to grid[i + 1][j]
        4 -> up    --- from grid[i][j] to grid[i - 1][j]
        '''
        m, n = len(grid), len(grid[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        cellCost = {}
        queue = collections.deque([(0, 0, 0)])
        while queue:
            row, col, cost = queue.popleft()
            while m > row >= 0 <= col < n and (row, col) not in cellCost:
                if row == m - 1 and col == n - 1:
                    return cost
                cellCost[(row, col)] = cost
                for x, y in direction:
                    queue.append((row + x, col + y, cost + 1))
                x, y = direction[grid[row][col] - 1]
                row, col = row + x, col + y
