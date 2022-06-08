from math import floor, log10

class Solution:
    def maximum69Number (self, num: int) -> int:
        n = num
        while n:
            div = 10 ** floor(log10(n))
            if n // div == 6:
                num += 3 * div
                break
            else:
                n = n % div
        return num
