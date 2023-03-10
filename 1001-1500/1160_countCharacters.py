from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char = Counter(chars)
        result = 0
        for word in words:
            if not (Counter(word) - char):
                result += len(word)
        return result
