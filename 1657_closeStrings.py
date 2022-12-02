class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)
        if len(set(c1.keys()) - set(c2.keys())) > 0: return False
        c1 = sorted([v for v in c1.values()])
        c2 = sorted([v for v in c2.values()])
        return c1 == c2
