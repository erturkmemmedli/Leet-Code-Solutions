class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        problems = set()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    problems.add(i)
                else:
                    stack.pop()
        if stack:
            [problems.add(i) for i in stack]
        result = ""
        for i, char in enumerate(s):
            if i not in problems:
                result += char
        return result
