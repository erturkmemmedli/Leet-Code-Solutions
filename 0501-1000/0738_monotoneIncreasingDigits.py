class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num = str(n)
        stack = []
        for digit in num:
            if not stack:
                stack.append(int(digit))
                continue
            dig = int(digit)
            if dig >= stack[-1]:
                stack.append(dig)
            else:
                stack[-1] -= 1
                while len(stack) > 1 and stack[-1] < stack[-2]:
                    stack.pop()
                    stack[-1] -= 1
                break
        stack += [9] * (len(num) - len(stack))
        answer = 0
        for i in range(len(stack)):
            answer += stack[i] * 10 ** (len(stack) - i - 1)
        return answer
