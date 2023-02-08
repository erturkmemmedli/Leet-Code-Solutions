from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, val in Counter(nums).most_common(k)]

# Alternative solution

from heapq import heappop, heappush
from collections import defaultdict

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = defaultdict(int)
        for num in nums:
            D[num] += 1
        heap = []
        for key, val in D.items():
            heappush(heap, (val, key))
            if len(heap) > k:
                heappop(heap)
        return [b for a, b in heap]

# Alternative solution

from heapq import heappop, heappush
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key, val in counter.items():
            if len(heap) < k:
                heappush(heap, (val, key))
            else:
                if val > heap[0][0]:
                    heappop(heap)
                    heappush(heap, (val, key))
        return [k for _, k in heap]
