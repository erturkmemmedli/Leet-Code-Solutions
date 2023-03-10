class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = 0
        for i in range(1, n+1):
            if n % i == 0:
                factor += 1
                if factor == k:
                    return i
        return -1
