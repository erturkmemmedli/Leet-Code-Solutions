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

# Alternative solution

class Solution1:
    def removeDuplicates(self, s: str) -> str:
        stack = ""
        for char in s:
            if stack and stack[-1] == char: stack = stack[:len(stack)-1]
            else: stack += char
        return stack
    
# Alternative solution

class Solution2:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char: stack.pop()
            else: stack.append(char)
        return ''.join(stack)
