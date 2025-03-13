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

# Alternative solution

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        i = 0
        while i < len(num):
            while stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
                if k == 0:
                    break 
            stack.append(num[i])
            i += 1
            if k == 0:
                break

        while k:
            stack.pop()
            k -= 1

        j = 0     
        while j < len(stack):
            if stack[j] == '0':
                j += 1
            else:
                break

        result = "".join(stack[j:])
        
        if result:
            result += num[i:]
            return result

        while i < len(num):
            if num[i] == '0':
                i += 1
            else:
                break
            
        result = num[i:]
        return result if result else "0"

# Alternative solution

sys.set_int_max_str_digits(10 ** 5)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i, digit in enumerate(num):
            while stack and stack[-1] > digit:
                stack.pop()
                k -= 1

                if k == 0:
                    return str(int("".join(stack) + num[i:]))
            
            stack.append(digit)
        
        return str(int("".join(stack)[:-k])) if stack and len(stack) != k else "0"

# Alternative solution

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()

        for i in range(len(num)):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1

            stack.append(num[i])

        for _ in range(k): stack.pop()

        while len(stack) > 1 and stack[0] == '0':
            stack.popleft()

        return "".join(stack) or '0'
