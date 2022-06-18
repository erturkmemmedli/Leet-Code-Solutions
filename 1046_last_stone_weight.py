import heapq as H

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        stones = [-i for i in stones]
        H.heapify(stones)
        while len(stones) > 1:
            y = H.heappop(stones)
            x = H.heappop(stones)
            if x == y:
                continue
            else:
                H.heappush(stones, y-x)
        return 0 if not stones else -1 * stones[0]
