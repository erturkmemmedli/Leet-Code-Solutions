class Solution:
    def findComplement(self, num: int) -> int:
        count = 0
        n = num
        while n != 1:
            n = n >> 1
            count += 1
        for _ in range(count + 1):
            n = n << 1
        return n - 1 - num
