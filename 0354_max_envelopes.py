from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: [x[0], -x[1]])
        heights = [j for i, j in envelopes]
        LIS = []
        for height in heights:
            index = bisect_left(LIS, height)
            LIS[index : index + 1] = [height]
        return len(LIS)
