class Solution:
    def bitwiseComplement(self, n: int) -> int:
        count = 0
        temp = n
        while temp:
            count += 1
            temp = temp >> 1
        top = 1
        for _ in range(count):
            top = top << 1
        if top > 1: top -= 1
        return top - n
