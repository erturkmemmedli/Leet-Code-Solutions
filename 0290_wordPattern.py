class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        S = s.split()
        if len(pattern) != len(S): return False
        D1 = {}
        D2 = {}
        for i, char in enumerate(pattern):
            if char not in D1:
                D1[char] = S[i]
            else:
                if D1[char] != S[i]: return False
            if S[i] not in D2:
                D2[S[i]] = char
            else:
                if D2[S[i]] != char: return False
        return True
