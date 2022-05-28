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

# Alternative solution

from collections import Counter

class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter(s2[:len(s1)])
        if target == window:
                return True
        for index, char in enumerate(s2[len(s1):], len(s1)):
            temp = s2[index - len(s1)]
            window[temp] -= 1
            if not window[temp]: del(window[temp])
            if char not in window: window[char] = 1
            else: window[char] += 1
            if target == window:
                return True
        return False
