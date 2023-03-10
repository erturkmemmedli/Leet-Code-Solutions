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

# Alternative solution

from collections import Counter
from math import ceil

class Solution1:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        limit = ceil(n/2)
        counter = Counter(arr).most_common()
        answer = 0
        i = 0
        while limit > 0:
            limit -= counter[i][1]
            i += 1
            answer += 1
        return answer
