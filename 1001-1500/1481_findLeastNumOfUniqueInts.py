class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        heap = []
        for key, val in c.items():
            heapq.heappush(heap, (val, key))
        while k:
            if not heap:
                return 0
            count, num = heapq.heappop(heap)
            if count > k:
                return len(heap) + 1
            elif count == k:
                return len(heap)
            else:
                k -= count
        return len(heap)

# Alternative solution

import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = dict()
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
        while k > 0 and heap:
            count, _ = heapq.heappop(heap)
            k -= count
        return len(heap) if k >= 0 else len(heap) + 1
