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
