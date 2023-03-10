from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return not (Counter(s) - Counter(t) or Counter(t) - Counter(s))
      
# Alternative solution

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
      
# Alternative solution   

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for i in s:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for i in t:
            if i not in dictionary:
                dictionary[i] = -1
            else:
                dictionary[i] -= 1
        for v in dictionary.values():
            if v:
                return False
        return True

# Alternative solution

from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
