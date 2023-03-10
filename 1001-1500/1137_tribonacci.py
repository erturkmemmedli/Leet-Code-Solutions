class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        first, second, third = 0, 1, 1
        for _ in range(n-2):
            first, second, third = second, third, first + second + third
        return third

# Alternative solution

class Solution:
    def __init__(self):
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1

        if n == 2:
            return 1

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        return self.memo[n]
