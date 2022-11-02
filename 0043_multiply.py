class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convert(num1) * self.convert(num2))

    def convert(self, num):
        result = 0
        for i, digit in enumerate(num):
            result += (ord(digit) - 48) * 10 ** (len(num) - i - 1)
        return result
