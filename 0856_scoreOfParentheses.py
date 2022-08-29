class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        output = 0
        stack = []
        answer = []
        for i, paranthes in enumerate(s):
            if paranthes == '(':
                stack.append(i)
            else:
                index = stack.pop()
                result = 0
                if answer and answer[-1][0] == index:
                    while answer and answer[-1][0] == index:
                        idx, val = answer.pop()
                        result += val
                    result *= 2
                    if stack:
                        answer.append((stack[-1], result))
                    else:
                        output += result
                else:
                    if stack:
                        answer.append((stack[-1], 1))
                    else:
                        output += 1
        return output
