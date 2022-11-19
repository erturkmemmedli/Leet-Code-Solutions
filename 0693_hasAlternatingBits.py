class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        count = 0
        temp = n
        while temp != 1:
            temp = temp >> 1
            count += 1
        for _ in range(count + 1):
            temp = temp << 1
        temp -= 1
        return n + (n>>1) == temp
