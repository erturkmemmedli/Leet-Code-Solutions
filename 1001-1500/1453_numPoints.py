class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        max_point = 0

        for x, y in darts:
            angles = []

            for x1, y1 in darts:
                distance = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5

                if (x != x1 or y != y1) and distance <= 2 * r:
                    angle = atan2(y1 - y, x1 - x)
                    delta = acos(distance / (2 * r))
                    angles.append((angle - delta, 1)) # entry
                    angles.append((angle + delta, -1)) # exit
                
            angles.sort(key = lambda x: [x[0], -x[1]])
            value = 1

            for _, entry in angles:
                value += entry
                max_point = max(max_point, value)

        return max_point
