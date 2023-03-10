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

# Alternative solution

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            distance = self.squaredEuclideanDistance(points[i])
            heapq.heappush(heap, (-distance, points[i]))
        for i in range(k, len(points)):
            distance = self.squaredEuclideanDistance(points[i])
            if distance < -heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, points[i]))
        return [pts for _, pts in heap]
            
    def squaredEuclideanDistance(self, point):
        x, y = point
        return x ** 2 + y ** 2
