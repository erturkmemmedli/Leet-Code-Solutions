from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_twos = []
        int_to_str = str(n)
        m = 1
        while m <= 10**9:
            pow_two_str = str(m)
            if len(pow_two_str) > len(int_to_str):
                break
            elif len(pow_two_str) == len(int_to_str):
                power_of_twos.append(pow_two_str)
            m <<= 1
        for num in power_of_twos:
            if len(Counter(num) - Counter(int_to_str)) == 0:
                return True
        return False
