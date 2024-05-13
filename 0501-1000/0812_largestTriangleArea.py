class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        largest_area = 0

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                    c = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)

                    s = (a + b + c) / 2
                    heron = s * (s - a) * (s - b) * (s - c)
                    if heron > 0:
                        area = math.sqrt(heron)
                        largest_area = max(largest_area, area)

        return largest_area
