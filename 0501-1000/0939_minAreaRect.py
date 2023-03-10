class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        for a, b in points:
            points_set.add((a, b))
        result = inf
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2:
                    if (x1, y2) in points_set and (x2, y1) in points_set:
                        result = min(result, (x1 - x2) * (y1 - y2))
        return result if result != inf else 0
