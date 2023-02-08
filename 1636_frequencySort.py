import heapq
import collections

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (v, -k))
        sortedArray = []
        for _ in range(len(heap)):
            count, num = heapq.heappop(heap)
            for i in range(count):
                sortedArray.append(-num)
        return sortedArray
