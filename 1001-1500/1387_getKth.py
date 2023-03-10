from heapq import heappush, heappop

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        for i in range(lo, hi+1):
            heappush(heap, (self.calculate_power(i), i))
        for _ in range(k-1):
            heappop(heap)
        return heappop(heap)[1]
        
    def calculate_power(self, x):
        count = 0
        while x != 1:
            if x % 2 == 0:
                x = x // 2
                count += 1
            else:
                x = 3 * x + 1
                count += 1
        return count
      
# Alternative solution

from heapq import heappush, heappop

class Solution1:
    def __init__(self):
        self.memo = {}
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        for i in range(lo, hi+1):
            heappush(heap, (self.calculate_power(i), i))
        for _ in range(k-1):
            heappop(heap)
        return heappop(heap)[1]
        
    def calculate_power(self, x):
        if x == 1: return 0
        if x in self.memo: return self.memo[x]
        if x % 2 == 0:
            res = 1 + self.calculate_power(x // 2) 
        else:
            res = 1 + self.calculate_power(3 * x + 1)
        self.memo[x] = res
        return res
