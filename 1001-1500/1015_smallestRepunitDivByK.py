import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        l = len(str(k))
        num = int('1' * l)

        for _ in range(1000000):
            if num % k == 0:
                return len(str(num))
            
            num = num * 10 + 1
        
        return -1
