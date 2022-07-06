class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        p = 0
        small = 0
        while n // 10 ** p > 10:
            x = n // 10 ** p
            if x % 10 == 9:
                small += 10 ** p
            else:
                small += (x % 10 + 1) * 10 ** p
            p += 1
        if small == 0: small = 1
        return [small, n-small]
