class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = collections.Counter(barcodes)
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        output = []
        while len(heap) > 1:
            a, b = heapq.heappop(heap)
            c, d = heapq.heappop(heap)
            output.extend([b, d])
            if a + 1 != 0:
                heapq.heappush(heap, (a + 1, b))
            if c + 1 != 0:
                heapq.heappush(heap, (c + 1, d))
        if heap:
            output.append(heapq.heappop(heap)[1])
        return output
