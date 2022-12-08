class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 1 which means a street connecting the left cell and the right cell.
        # 2 which means a street connecting the upper cell and the lower cell.
        # 3 which means a street connecting the left cell and the lower cell.
        # 4 which means a street connecting the right cell and the lower cell.
        # 5 which means a street connecting the left cell and the upper cell.
        # 6 which means a street connecting the right cell and the upper cell.
        m, n = len(grid), len(grid[0])
        streetMap = {
                     1: ([(0, -1), {1, 4, 6}], [(0, 1), {1, 3, 5}]),
                     2: ([(1, 0), {2, 5, 6}], [(-1, 0), {2, 3, 4}]),
                     3: ([(0, -1), {1, 4, 6}], [(1, 0), {2, 5, 6}]),
                     4: ([(0, 1), {1, 3, 5}], [(1, 0), {2, 5, 6}]),
                     5: ([(0, -1), {1, 4, 6}], [(-1, 0), {2, 3, 4}]),
                     6: ([(0, 1), {1, 3, 5}], [(-1, 0), {2, 3, 4}])
                     }
        queue = collections.deque([(0, 0)])
        visited = {(0, 0)}
        while queue:
            row, col = queue.popleft()
            if (row, col) == (m - 1, n - 1):
                return True
            street = grid[row][col]
            for direction, roads in streetMap[street]:
                x, y = direction
                if m > row + x >= 0 <= col + y < n and grid[row + x][col + y] in roads and (row + x, col + y) not in visited:
                    queue.append((row + x, col + y))
                    visited.add((row + x, col + y))
        return False
