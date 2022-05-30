class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend
        b = divisor
        if a // b > 0:
            return a//b if a//b < 2**31 - 1 else 2**31 - 1
        else:
            return -(abs(a)//abs(b)) if abs(a)//abs(b) < 2**31 else -2**31
            
# Alternative solution   

class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:
        is_positive = (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) 
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temporary = divisor
            increment = 1
            while dividend >= temporary:
                dividend -= temporary
                quotient += increment
                temporary <<= 1
                increment <<= 1
        if not is_positive:
            quotient *= -1
        return min(max(-2**31, quotient), 2**31 - 1)
