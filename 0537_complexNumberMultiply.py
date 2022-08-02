class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        for i, ch in enumerate(num1):
            if ch == '+':
                break
        real1 = int(num1[:i])
        imaginary1 = int(num1[i+1:-1])
        for j, ch in enumerate(num2):
            if ch == '+':
                break
        real2 = int(num2[:j])
        imaginary2 = int(num2[j+1:-1])
        real = real1 * real2 - imaginary1 * imaginary2
        imaginary = real1 * imaginary2 + real2 * imaginary1
        return str(real) + '+' + str(imaginary) + 'i'
