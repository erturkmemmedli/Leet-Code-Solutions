class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ones = [(row.count(1), i)  for i, row in enumerate(mat)]
        order = [i[1] for i in sorted(ones, key = lambda x: x[0])]
        return order[:k]

# Alternative solution

import heapq as H

class Solution1:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ones = [(row.count(1), i)  for i, row in enumerate(mat)]
        H.heapify(ones)
        return [H.heappop(ones)[1] for _ in range(k)]
