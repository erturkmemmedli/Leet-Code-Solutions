class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        time = 0
        for i in range(1, n):
            maximum = max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
            minimum = min(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1]))
            time += minimum
            time += (maximum - minimum)
        return time
