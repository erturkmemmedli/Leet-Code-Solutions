class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int: 
        n = len(profits)
        projects = sorted(list(zip(capital, profits)))
        heap = []
        unavailable = 0
        for i in range(k):
            while unavailable < n and projects[unavailable][0] <= w:
                heappush(heap, -projects[unavailable][1])
                unavailable += 1
            if not heap:
                break
            w -= heappop(heap)
        return w
