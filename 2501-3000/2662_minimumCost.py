class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        specialRoads = [[a, b, c, d, w] for a, b, c, d, w in specialRoads if w < abs(a - c) + abs(b - d)]
        result = abs(target[0] - start[0]) + abs(target[1] - start[1])
        distance = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]

        while heap:
            dist, row, col = heappop(heap)
            for a, b, c, d, w in specialRoads:
                if distance.get((c, d), inf) > dist + abs(row - a) + abs(col - b) + w:
                    distance[(c, d)] = dist + abs(row - a) + abs(col - b) + w
                    heappush(heap, (distance[(c, d)], c, d))

        for a, b, c, d, w in specialRoads:
            result = min(result, distance.get((c, d), inf) + abs(target[0] - c) + abs(target[1] - d))
        
        return result
