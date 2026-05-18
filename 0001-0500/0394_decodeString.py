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

# Alternative solution

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", ""]]
        for i, char in enumerate(s):
            if char.isdigit():
                if i == 0 or not s[i-1].isdigit():
                    stack.append(["", ""])
                stack[-1][0] += char
            elif char.isalpha():
                stack[-1][1] += char
            elif char == ']':
                m, t = stack.pop()
                if stack:
                    stack[-1][1] += t * int(m)
                else:
                    stack = [["", ""]]
        return stack[0][1]
