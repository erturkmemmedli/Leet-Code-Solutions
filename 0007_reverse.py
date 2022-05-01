class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            n = len(str(x)) - 1
        else:
            n = len(str(x))
        result = 0
        if x < 0:
            x *= -1
            for i in range(n):
                result += x % 10 ** (n - i) // 10 ** (n - i - 1) * 10 ** i
                if -1 * result < -2 ** 31:
                    return 0
            return -1 * result
        else:
            for i in range(n):
                result += x % 10 ** (n - i) // 10 ** (n - i - 1) * 10 ** i
                if result >= 2 ** 31 - 1:
                    return 0
            return result