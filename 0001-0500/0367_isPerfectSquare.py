class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = int(num ** 0.5)
        return x ** 2 == num
      
# Alternative solution

class Solution1:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        m = (l+r) // 2
        while l <= r:
            if m ** 2 == num:
                return True
            if m ** 2 > num:
                r = m-1
                m = (l+r) // 2
            if m ** 2 < num:
                l = m + 1
                m = (l+r) // 2
        return False
