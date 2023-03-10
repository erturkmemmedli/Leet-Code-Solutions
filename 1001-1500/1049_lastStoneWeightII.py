class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        knapsack = {0}
        total = sum(stones)
        for stone in stones:
            knapsack = {stone + item for item in knapsack} | {abs(stone - item) for item in knapsack}
        return min(knapsack)
