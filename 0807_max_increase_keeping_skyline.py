class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        horizontal = list(map(lambda x: max(x), grid))
        vertical = list(map(lambda x: max(x), list(zip(*grid))))
        max_total_sum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_total_sum += min(horizontal[row], vertical[col]) - grid[row][col]
        return max_total_sum
