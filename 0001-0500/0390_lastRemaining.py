class Solution:
    def lastRemaining(self, n: int) -> int:
        return self.recursion(n, 0)

    def recursion(self, n, reverse):
        if n == 1:
            return 1
        if not reverse:
            return 2 * self.recursion(n//2, 1)
        if n % 2 == 1:
            return 2 * self.recursion(n//2, 0)
        else:
            return 2 * self.recursion(n//2, 0) - 1
