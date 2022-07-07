class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if not n or n & n-1:
            return False
        else:
            return self.count_ones(n-1) % 2 == 0
            
    def count_ones(self, n):
        count = 0
        while n:
            count += 1
            n = n & n-1
        return count

# Alternative solution

class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0: return False
        if n == 1: return True
        return self.isPowerOfFour(n//4) if n % 4 == 0 else False
