class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n % 2 == 0 and n > 0:
            n = n >> 1
        return n == 1

# Alternative solution

class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not n & (n-1)