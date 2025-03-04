class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 2:
            if n % 3 == 2:
                return False
            elif n % 3 == 1:
                n -= 1
            else:
                n //= 3
            
        return n != 2
