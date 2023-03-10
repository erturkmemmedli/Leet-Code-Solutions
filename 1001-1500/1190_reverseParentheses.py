class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                s = s[:j] + s[j+1:i][::-1] + s[i+1:]
                i -= 2
            i += 1
        return s
