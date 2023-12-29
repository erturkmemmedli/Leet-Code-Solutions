class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        idx = 0

        while n:
            if n % 2 == 1:
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            
            idx += 1
            n //= 2

        return [even, odd]
