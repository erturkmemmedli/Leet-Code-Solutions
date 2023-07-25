class Solution:
    def getSum(self, a: int, b: int) -> int:

        def add(a, b):
            if b == 0:
                return a

            xor = a ^ b
            and_shift = (a & b) << 1

            return add(xor, and_shift)

        if a * b < 0:
            if a > 0:
                return self.getSum(b, a)

            if add(~a, 1) == b:
                return 0

            if add(~a, 1) < b:
                return add(~add(add(~a, 1), add(~b, 1)), 1)

        return add(a, b)

# Alternative solution

class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF

        while (b & mask) > 0:
            xor = a ^ b
            and_shift = (a & b) << 1

            a, b = xor, and_shift

        return a if b <= 0 else (a & mask)
