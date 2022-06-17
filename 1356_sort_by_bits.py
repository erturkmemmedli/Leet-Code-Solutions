import heapq

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        count = [(bin(i).count('1'), i) for i in arr]
        heapq.heapify(count)
        return [heapq.heappop(count)[1] for _ in range(len(arr))]
      
# Alternative solution

class Solution1:
    def sortByBits(self, arr: List[int]) -> List[int]:
        count = [(bin(i).count('1'), i) for i in arr]
        order = [i[1] for i in sorted(count, key = lambda x: (x[0], x[1]))]
        return order
