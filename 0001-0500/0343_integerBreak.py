class Solution:
    def integerBreak(self, n: int) -> int:
        hashmap = {1: 0}
        for i in range(2, n+1):
            result = 0
            for j in range(1, i//2 + 1):
                result = max(result, max(i-j, hashmap[i-j]) * max(j, hashmap[j]))
            hashmap[i] = result
        return hashmap[n]
