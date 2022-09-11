from collections import Counter
from heapq import heapify, heappop, heappush
from math import ceil

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        limit = ceil(n/2)
        c = Counter(arr)
        h = []
        heapify(h)
        for v in c.values():
            heappush(h, -v)
        answer = 0
        while limit > 0:
            limit += heappop(h)
            answer += 1
        return answer
