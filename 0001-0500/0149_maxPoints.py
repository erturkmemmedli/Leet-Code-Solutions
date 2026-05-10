class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        answer = 1

        for i in range(len(points)):
            slopes = defaultdict(int)

            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0]:
                    slopes["inf"] += 1
                    answer = max(answer, slopes["inf"])
                else:
                    slope = self.calculateSlope(points[i], points[j])
                    slopes[slope] += 1
                    answer = max(answer, slopes[slope])

        return answer + 1

    def calculateSlope(self, pts1, pts2):
        x1, y1 = pts1
        x2, y2 = pts2
        slope = (y2 - y1) / (x2 - x1)
        return slope

# Alternative solution

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calculateSlope(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else 'inf'

        answer = 1
        for i in range(len(points)):
            slope_map = defaultdict(int)
            for j in range(i + 1, len(points)):
                slope = calculateSlope(points[i], points[j])
                slope_map[slope] += 1
                answer = max(answer, slope_map[slope] + 1)
        return answer
