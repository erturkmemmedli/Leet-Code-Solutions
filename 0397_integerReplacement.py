class Solution:
    def integerReplacement(self, n: int) -> int:
        if n <= 3: return n - 1
        operation = 0
        while n > 3:
            if n % 2 == 0:
                n //= 2
            else:
                if (n + 1) % 4 == 0:
                    n += 1
                else:
                    n -= 1
            operation += 1
        return operation + n - 1
