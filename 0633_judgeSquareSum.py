class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = int(c ** 0.5)
        b = 0
        while a >= b:
            if a ** 2 + b ** 2 == c:
                return True
            elif a ** 2 + b ** 2 < c:
                b += 1
            else:
                a -= 1
        return False
