class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        L = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if (65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122) and (65 <= ord(s[j]) <= 90 or 97 <= ord(s[j]) <= 122):
                L[i], L[j] = L[j], L[i]
                i += 1
                j -= 1
            elif 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
                j -= 1
            elif 65 <= ord(s[j]) <= 90 or 97 <= ord(s[j]) <= 122:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(L)
