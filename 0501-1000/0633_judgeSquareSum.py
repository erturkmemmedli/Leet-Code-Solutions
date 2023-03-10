class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = int(c ** 0.5)
        b = 0
        while a >= b:
            sq_sum = a ** 2 + b ** 2
            if sq_sum == c:
                return True
            elif sq_sum < c:
                b += 1
            else:
                a -= 1
        return False
