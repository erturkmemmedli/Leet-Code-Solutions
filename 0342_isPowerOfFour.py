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
