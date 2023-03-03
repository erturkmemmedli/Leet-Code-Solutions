class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        prev = 0
        curr = 1
        for _ in range(n-1):
            curr, prev = curr + prev, curr
        return curr

# Alternative solution

class Solution:
    def fib(self, n: int) -> int:
        self.memo = {}
        return self.dp(n)

    def dp(self, n):
        if n <= 1:
            return n
        
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.dp(n-1) + self.dp(n-2)
        return self.memo[n]
