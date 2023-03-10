class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.memo = {}
        return self.dp(n, k, target) % (10 ** 9 + 7)

    def dp(self, n, k, target):
        if (n, target) in self.memo:
            return self.memo[(n, target)]
        if n == 1:
            if k >= target >= n:
                self.memo[(n, k, target)] = 1
                return 1
            return 0
        result = 0
        for i in range(1, k + 1):
            result += self.dp(n - 1, k, target - i)
        self.memo[(n, target)] = result
        return result
        
# ALternative solution

class Solution1:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.memo = {}
        return self.dp(n, k, target) % (10 ** 9 + 7)

    def dp(self, n, k, target):
        if n == 0:
            return 0 if target > 0 else 1
        if (n, target) in self.memo:
            return self.memo[(n, target)]
        result = 0
        for i in range(max(0, target - k), target):
            result += self.dp(n - 1, k, i)
        self.memo[(n, target)] = result
        return result
