class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        current_position = points[0][1]
        number_of_arrows = 1
        for i in range(1, len(points)):
            if points[i][0] <= current_position:
                current_position = min(current_position, points[i][1])
                continue
            else:
                number_of_arrows += 1
                current_position = points[i][1]
        return number_of_arrows
