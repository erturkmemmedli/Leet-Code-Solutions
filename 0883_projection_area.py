class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum([grid[i][j] != 0 for i in range(len(grid)) for j in range(len(grid[0]))])
        front = sum([max(i) for i in grid])
        array = grid[0]
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                array[j] = max(array[j], grid[i][j])
        side = sum(array)
        return top + front + side
