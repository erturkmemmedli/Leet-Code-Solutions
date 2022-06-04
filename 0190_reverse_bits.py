class Solution:
    def reverseBits(self, n: int) -> int:
        step = 0
        result = 0
        while n:
            if n & 1:
                result += 2 ** (31 - step)
                step += 1
                n = n >> 1
            else:
                step += 1
                n = n >> 1
        return result
