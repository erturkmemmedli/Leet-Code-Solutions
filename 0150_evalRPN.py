class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['*', '/', '+', '-']:
                stack.append(int(token))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    stack.append(a + b)
                if token == '-':
                    stack.append(a - b)
                if token == '*':
                    stack.append(a * b)
                if token == '/':
                    if (a < 0 and b > 0) or (a > 0 and b < 0):
                        stack.append(-(-a // b))
                    else:
                        stack.append(a // b)
        return stack[0]
