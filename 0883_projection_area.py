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

# Alternative solution

class Solution1:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum([cell > 0 for array in grid for cell in array])
        front = sum([max(array) for array in grid])
        side = sum([max(pair) for pair in zip(*grid)])
        return top + front + side
