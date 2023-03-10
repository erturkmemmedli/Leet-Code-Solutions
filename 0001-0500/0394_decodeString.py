class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        mul = []
        temp = ''
        while i < len(s):
            if s[i] == '[':
                stack.append(i)
                mul.append(temp)
                temp = ''
            elif s[i].isdigit():
                temp += s[i]
            elif s[i] == ']':
                j = stack.pop()
                m = mul.pop()
                l = len(m)
                m = int(m)
                s = s[:j-l] + m * s[j+1:i] + s[i+1:]
                i = j - l - 1 + m * (i - j - 1)
            i += 1
        return s
