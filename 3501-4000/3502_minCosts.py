class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        for i in range(1, len(cost)):
            cost[i] = cost[i - 1] if cost[i] > cost[i - 1] else cost[i]
        return cost
