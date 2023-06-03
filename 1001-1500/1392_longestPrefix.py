class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(1, len(s)):
            if s[:-i] == s[i:]:
                return s[i:]
        return ""

# Alternative solution

class Solution:
    def longestPrefix(self, s: str) -> str:
        res, l, r, mod = 0, 0, 0, 10**9 + 7

        for i in range(len(s) - 1):
            l = (l * 128 + ord(s[i])) % mod
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod
            if l == r: res = i + 1

        return s[:res]
