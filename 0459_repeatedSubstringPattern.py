class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = 1
        while j <= len(s)//2:
            if s[j] == s[0]:
                for i in range(j, len(s), j):
                    if s[:j] != s[i:i+j]:
                        break
                    if s[:j] == s[j:2*j] and i == len(s)-j:
                        return True
            j += 1
        return False

# Alternative solution

class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]
