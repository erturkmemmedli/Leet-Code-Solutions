class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        set_x = set()
        set_y = set()
        for x, y in coordinates:
            set_x.add(x)
            set_y.add(y)
        if len(set_x) == 1 or len(set_y) == 1:
            return True
        elif len(set_x) != len(coordinates) or len(set_y) != len(coordinates):
            return False
        x = coordinates[1][0] - coordinates[0][0]
        y = coordinates[1][1] - coordinates[0][1]
        slope = y / x
        for i in range(2, len(coordinates)):
            a = coordinates[i][0] - coordinates[i-1][0]
            b = coordinates[i][1] - coordinates[i-1][1]
            if b/a != slope:
                return False
        return True

# Alternative solution

class Solution1:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for x, y in coordinates[2:]:
            if (x - x2) * (y2 - y1) != (x2 - x1) * (y - y2):
                return False
        return True
