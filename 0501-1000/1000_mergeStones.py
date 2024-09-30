class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        if k > 2 and n % (k - 1) != 1:
            return -1
        
        prefix = [0] * (n + 1)
        memo = {}

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        
        def dp(i, j, pile):
            if i == j and pile == 1:
                return 0

            if (i, j, pile) in memo:
                return memo[(i, j, pile)]

            if pile == 1:
                memo[(i, j, pile)] = dp(i, j, k) + prefix[j + 1] - prefix[i]
                return memo[(i, j, pile)] 

            else:
                min_cost = float('inf')

                for x in range(i, j, k - 1):
                    min_cost = min(min_cost, dp(i, x, 1) + dp(x + 1, j, pile - 1))
                
                memo[(i, j, pile)] = min_cost
                return memo[(i, j, pile)]

        return dp(0, n - 1, 1)
