class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3: return False
        stack = []
        for char in s:
            if char == 'a':
                stack.append(char)
            elif char == 'b':
                if len(stack) < 1: return False
                if stack[-1] != 'a': return False
                stack.append(char)
            elif char == 'c':
                if len(stack) < 2: return False
                if stack[-1] != 'b': return False
                stack.pop()
                stack.pop()
        return not stack
