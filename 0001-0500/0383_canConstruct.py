class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        for i in magazine:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for i in ransomNote:
            if i not in dictionary:
                dictionary[i] = -1
            else:
                dictionary[i] -= 1
        for k, v in dictionary.items():
            if v < 0:
                return False
        return True
      
# Alternative solution
 
from collections import Counter

class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
