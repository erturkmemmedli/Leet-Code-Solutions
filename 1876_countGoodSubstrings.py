class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        distinct = 0
        for i in range(len(s) - 2):
            w = s[i:i+3]
            if w[0] != w[1] and w[0] != w[2]  and w[1] != w[2]:
                distinct += 1
        return distinct
