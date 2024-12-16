class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # advanced test case: [7,1,13,7,14,30,31]
        start = n // 2
        end = n
        increment = 0
        
        while start > 0:
            i = start
            
            while i < end:
                increment += abs(cost[i] - cost[i + 1])
                cost[i//2] += max(cost[i], cost[i + 1])
                i += 2
            
            end = start
            start //= 2

        return increment
