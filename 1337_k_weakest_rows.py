class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ones = [(row.count(1), i)  for i, row in enumerate(mat)]
        order = [i[1] for i in sorted(ones, key = lambda x: x[0])]
        return order[:k]
