class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convert(num1) * self.convert(num2))

    def convert(self, num):
        result = 0
        for i, digit in enumerate(num):
            result += (ord(digit) - 48) * 10 ** (len(num) - i - 1)
        return result

# Alternative solution

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num):
            res = 0
            for i in range(len(num)-1, -1, -1):
                res += (ord(num[i]) - 48) * 10 ** (len(num) - i - 1)
            return res

        num1 = convert(num1)
        num2 = convert(num2)
        mult = num1 * num2

        if not mult: return "0"

        output = ""

        while mult:
            mod = mult % 10
            output += chr(mod + 48)
            mult //= 10

        return output[::-1]
