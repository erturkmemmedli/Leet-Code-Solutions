from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, [x, y] in enumerate(points):
            distance = x * x + y * y
            heappush(heap, (distance, i))
        output = []
        for _ in range(k):
            output.append(points[heappop(heap)[1]])
        return output
