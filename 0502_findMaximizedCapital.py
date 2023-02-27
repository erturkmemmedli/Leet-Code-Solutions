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

# Alternative solution

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        usableHeap = []
        reserveHeap = []

        for i in range(len(profits)):
            if capital[i] <= w:
                heappush(usableHeap, (-profits[i], capital[i]))
            else:
                heappush(reserveHeap, (capital[i], profits[i]))
    
        while k:
            if not usableHeap:
                break
                
            profit, capital = heappop(usableHeap)
            w -= profit
            k -= 1

            while reserveHeap and reserveHeap[0][0] <= w:
                capital, profit = heappop(reserveHeap)
                heappush(usableHeap, (-profit, capital))

        return w
