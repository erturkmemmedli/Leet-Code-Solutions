class Solution:
    def maxPower(self, s: str) -> int:
        mx = 1
        ct = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                ct += 1
                mx = max(mx, ct)                
            else:
                ct = 1
        return mx
