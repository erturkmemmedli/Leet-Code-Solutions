class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * 1001
        for num, fr, to in trips:
            if num > capacity: return False
            locations[fr] += num
            locations[to] -= num
        for i in range(1, len(locations)):
            locations[i] += locations[i-1]
            if locations[i] > capacity: return False
        return True

# Alternative solution

from heapq import heappush, heappop

class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        heap = []
        current = 0
        for num, fr, to in trips:
            while heap and heap[0][0] <= fr:
                pop = heappop(heap)
                current -= pop[1]
            current += num
            if current > capacity: return False
            heappush(heap, (to, num))
        return True
