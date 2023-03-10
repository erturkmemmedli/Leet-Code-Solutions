class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = 0
        ones = 0
        flip = 0
        if s[0] == '0': zeros += 1
        else: ones += 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if zeros < ones:
                    flip = min(flip + 1, ones)
                zeros += 1
            if s[i] == '1':
                zeros = 0
                ones += 1
        return flip
