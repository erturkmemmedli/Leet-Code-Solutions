class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend
        b = divisor
        if a // b > 0:
            return a//b if a//b < 2**31 - 1 else 2**31 - 1
        else:
            return -(abs(a)//abs(b)) if abs(a)//abs(b) < 2**31 else -2**31
            
# Alternative solution   
