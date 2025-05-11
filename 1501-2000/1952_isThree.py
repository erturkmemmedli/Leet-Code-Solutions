class Solution:
    def isThree(self, n: int) -> bool:
        m = math.sqrt(n)

        if m != int(m) or m == 1:
            return False

        m = int(m)
        
        for i in range(2, m):
            if m % i == 0:
                return False
            
        return True
        
