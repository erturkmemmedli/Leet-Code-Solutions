class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return
        target = collections.Counter(p)
        source = Counter(s[0:len(p)])
        result = []
        if source == target:
            result.append(0)
        for i in range(len(p), len(s)):
            source[s[i - len(p)]] -= 1
            source[s[i]] += 1
            if source == target:
                result.append(i - len(p) + 1)
        return result
