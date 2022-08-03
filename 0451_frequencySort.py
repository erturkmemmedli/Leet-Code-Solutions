from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        C = Counter(s)
        C = sorted(C.items(), key = lambda x: x[1], reverse = True)
        output = ''
        for k, v in C:
            output += k * v
        return output
        
# Alternative solution

from collections import Counter

class Solution1:
    def frequencySort(self, s: str) -> str:
        C = Counter(s)
        output = ""
        for k, v in C.most_common():
            output += k * v
        return output
