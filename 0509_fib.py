class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        prev = 0
        curr = 1
        for _ in range(n-1):
            curr, prev = curr + prev, curr
        return curr
