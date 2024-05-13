class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0

        for decimal in range(left, right + 1):
            binary = bin(decimal)

            if binary.count('1') in primes:
                count += 1

        return count
