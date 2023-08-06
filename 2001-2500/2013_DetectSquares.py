from sortedcontainers import SortedList

class DetectSquares:
    def __init__(self):
        self.x_map = defaultdict(dict)
        self.y_map = defaultdict(dict)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_map[x][y] = self.x_map[x].get(y, 0) + 1
        self.y_map[y][x] = self.y_map[y].get(x, 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point
        cnt = 0
        for y0 in self.x_map[x]:
            count = self.x_map[x][y0]
            length = y - y0
            if length != 0:
                if y in self.x_map[x - length] and y0 in self.x_map[x - length]:
                    cnt += count * self.x_map[x - length][y] * self.x_map[x - length][y0]
                if y in self.x_map[x + length] and y0 in self.x_map[x + length]:
                    cnt += count * self.x_map[x + length][y] * self.x_map[x + length][y0]
        return cnt

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
