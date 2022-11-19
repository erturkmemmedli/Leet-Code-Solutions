from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        counter = Counter(sorted(s))
        chars = list(counter.keys())
        counts = list(counter.values())
        result = ""
        while len(counts) > 1:
            i = 0
            while i < len(counts):
                result += chars[i]
                counts[i] -= 1
                if counts[i]:
                    i += 1
                else:
                    counts.pop(i)
                    chars.pop(i)
            i = len(counts) - 1
            while i >= 0:
                result += chars[i]
                counts[i] -= 1
                if counts[i]:
                    i -= 1
                else:
                    counts.pop(i)
                    chars.pop(i)
                    i -= 1
        if chars:
            result += chars[0] * counts[0]
        return result
