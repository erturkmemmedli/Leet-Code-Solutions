from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        myset = set()
        for v in counter.values():
            if v in myset: return False
            myset.add(v)
        return True
