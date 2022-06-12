from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        x = Counter(words[0])
        for word in words:
            x = x - (x - Counter(word))
            if not x: return []
        result = []
        for k, v in x.items():
            result += [k] * v
        return result 
