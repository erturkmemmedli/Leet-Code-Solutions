class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            if sorted(s2[i:i+len(s1)]) == s1:
                return True
        return False

# Alternative solution

from collections import Counter

class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            c2 = Counter(s2[i:i+len(s1)])
            if not c1 - c2:
                return True
        return False  
