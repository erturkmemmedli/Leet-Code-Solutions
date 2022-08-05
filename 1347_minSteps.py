from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        C = Counter(t) - Counter(s)
        return sum(C.values())
