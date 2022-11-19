from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = Counter(nums)
        M = max(C.values())
        L = [k for k,v in C.items() if v == M]
        D = {num : [] for num in L}
        for i, num in enumerate(nums):
            if num in D:
                D[num].append(i)
        return min([D[k][-1] - D[k][0] + 1 for k in D.keys()])
