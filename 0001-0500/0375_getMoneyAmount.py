from functools import lru_cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return self.dp(1, n)

    @lru_cache(None) # using for memoization
    def dp(self, left, right):
        if left >= right:
            return 0
        answer = float('inf')
        for pick in range(left, right + 1):
            leftPick = self.dp(left, pick - 1) + pick
            rightPick = self.dp(pick + 1, right) + pick
            cost = max(leftPick, rightPick)
            answer = min(answer, cost)
        return answer
