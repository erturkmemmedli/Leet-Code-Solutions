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
        
# Alternative solution

class Solution1:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        x = abs(x)
        power = 0
        temp = x
        while temp:
            temp //= 10
            power += 1
        result = 0
        while power > 0:
            mod = x % 10
            x = x // 10
            result += mod * 10 ** (power - 1)
            power -= 1
        result = -result if negative else result
        return result if -2**31  <= result <= 2**31 - 1 else 0
