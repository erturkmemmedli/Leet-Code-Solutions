class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        chars = collections.Counter(s)
        odds = 0
        for ct in chars.values():
            if ct % 2 == 1:
                odds += 1
        return k - odds >= 0
