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

# Alternative solution

from collections import Counter, deque

class Solution3:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = deque()
        countWindow = Counter()
        for char in s2:
            if char not in target:
                window = deque()
                countWindow = Counter()
            else:
                if len(window) == len(s1):
                    pop = window.popleft()
                    if countWindow[pop] == 1: del countWindow[pop]
                    else: countWindow[pop] -= 1
                window.append(char)
                countWindow[char] += 1
                if countWindow == target: return True
        return False

# Alternative solution

class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        k = len(s1)
        map1 = {}
        for char in s1:
            if char not in map1:
                map1[char] = 1
            else:
                map1[char] += 1
        map2 = {}
        for i, char in enumerate(s2):
            if char not in map2:
                map2[char] = 1
            else:
                map2[char] += 1
            if i >= k:
                map2[s2[i - k]] -= 1
                if not map2[s2[i - k]]:
                    del map2[s2[i - k]]
            if map1 == map2:
                return True
        return False
