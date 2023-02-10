class Solution:
    def isHappy(self, n: int) -> bool:
        Set = set()
        while n not in Set:
            Set.add(n)
            num = str(n)
            x = 0
            for i in num:
                x += int(i) ** 2
            n = x
        return n == 1

# Alternative solution

class Solution:
    def isHappy(self, n: int) -> bool:
        fast = slow = n
        while fast != 1:
            fast = self.digitSquareSum(self.digitSquareSum(fast))
            if fast == 1:
                break
            slow = self.digitSquareSum(slow)
            if fast == slow:
                return False
        return True
            
    def digitSquareSum(self, n):
        res = 0
        while n:
            x = n % 10
            res += x ** 2
            n //= 10
        return res
