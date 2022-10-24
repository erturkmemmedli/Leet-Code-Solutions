class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[n] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        for i in range(n):
            left, right, up, down = 0, 0, 0, 0
            for j, k in zip(range(n), reversed(range(n))):
                left = left + 1 if grid[i][j] else 0
                if left < grid[i][j]:
                    grid[i][j] = left
                right = right + 1 if grid[i][k] else 0
                if right < grid[i][k]:
                    grid[i][k] = right
                up = up + 1 if grid[j][i] else 0
                if up < grid[j][i]:
                    grid[j][i] = up
                down = down + 1 if grid[k][i] else 0
                if down < grid[k][i]:
                    grid[k][i] = down
        answer = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > answer:
                    answer = grid[i][j]
        return answer

# Alternative solution (which gives TLE error)

from functools import lru_cache

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if len(mines) == n ** 2: return 0
        maximum = 1
        mines = tuple([(a, b) for a, b in mines])
        for i in range(1, n - 1):
            j = 1
            while j < n - 1:
                if j < maximum: j = maximum
                if (i, j) not in mines:
                    maximum = max(maximum, 1 + self.move(n, mines, (i, j), (i, j), (i, j), (i, j)))
                    if maximum == i + 1: break
                if n - j <= maximum: break
                if (i, j) in mines: j += maximum
                else: j += 1
            if n - i <= maximum: break
        return maximum

    @lru_cache(None)
    def move(self, n, mines, up, down, left, right):
        if (up[0] - 1 >= 0 and (up[0] - 1, up[1]) not in mines) and (
            down[0] + 1 < n and (down[0] + 1, down[1]) not in mines) and (
                left[1] - 1 >= 0 and (left[0], left[1] - 1) not in mines) and (
                    right[1] + 1 < n and (right[0], right[1] + 1) not in mines):
                        return 1 + self.move(n, mines,
                                            (up[0] - 1, up[1]),
                                            (down[0] + 1, down[1]),
                                            (left[0], left[1] - 1),
                                            (right[0], right[1] + 1))
        else: return 0
