class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        L = 0
        R = 0
        i = 0
        while i < len(s):
            if s[i] == 'L':
                L += 1
            if s[i] == 'R':
                R += 1
            if L == R:
                count += 1
                L == 0
                R == 0
            i += 1
        return count
