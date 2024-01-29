class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisable = 0
        non_divisable = 0

        for i in range(1, n + 1):
            if i % m == 0:
                divisable += i
            else:
                non_divisable += i

        return non_divisable - divisable
