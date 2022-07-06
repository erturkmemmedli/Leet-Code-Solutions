class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        if n == 0: return False
        if n % 3 == 0: return self.isPowerOfThree(n//3)
        
# Alternative solution

class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            num = str(n)
            if sum([int(i) for i in num]) % 3 != 0:
                return False
            n = n // 3
        return n == 1
