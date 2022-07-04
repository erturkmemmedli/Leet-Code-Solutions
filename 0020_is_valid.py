class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        for s in string:
            if s == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif s == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif s == ']':
                if not stack or stack.pop() != '[':
                    return False
            if s in ['(', '{', '[']:
                stack.append(s)
        return True if not stack else False

# Alternative solution

class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ['(', '[', '{']:
                stack.append(p)
            else:
                if not stack:
                    return False
                pop = stack.pop()
                if not (pop == '(' and p == ')') and not (pop == '[' and p == ']') and not (pop == '{' and p == '}'):
                    return False
        return True if not stack else False
