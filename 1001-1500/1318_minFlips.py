class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            odd = a % 2 or b % 2
            even = not odd
            if c % 2:
                if even:
                    count += 1
            else:
                if a % 2:
                    count += 1
                if b % 2:
                    count += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return count
