class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        j = 1
        while s and j < len(s):
            if s[i] == s[j] and i >= 0:
                s = s[:i] + s[j+1:]
                i -= 1
                j -= 1
            else:
                i += 1
                j += 1
        return s
