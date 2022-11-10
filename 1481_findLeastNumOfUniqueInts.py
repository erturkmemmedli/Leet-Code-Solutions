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
