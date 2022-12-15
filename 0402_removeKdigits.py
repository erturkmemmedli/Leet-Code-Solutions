class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return "0"
        num = list(num)
        stack = []
        while k > 0:
            for i in range(len(num)):
                while stack and stack[-1] > num[i] and k > 0:
                    stack.pop()
                    k -= 1
                if k == 0:
                    stack += num[i:]
                    break
                else:
                    stack.append(num[i])
            if k == 0:
                break
            elif len(stack) == len(num):
                stack = stack[:len(stack)-k]
                break
            else:
                num = stack[:]
                stack = []
        result = "".join(stack).lstrip("0")
        return result if result else "0"
