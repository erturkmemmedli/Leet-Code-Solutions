from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        mxm = -1
        for k, v in counter.items():
            if k == v:
                mxm = max(mxm, k)
        return mxm
