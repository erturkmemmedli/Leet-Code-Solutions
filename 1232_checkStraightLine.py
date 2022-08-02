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
