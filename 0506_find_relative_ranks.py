import heapq
import copy

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        reserved = copy.deepcopy(score)
        heapq.heapify(reserved)
        n = len(reserved)
        dictionary = {}
        while len(reserved) > 3:
            dictionary[heapq.heappop(reserved)] = str(n)
            n -= 1
        if len(reserved) == 3: dictionary[heapq.heappop(reserved)] = "Bronze Medal"
        if len(reserved) == 2: dictionary[heapq.heappop(reserved)] = "Silver Medal"
        if len(reserved) == 1: dictionary[heapq.heappop(reserved)] = "Gold Medal"
        return [dictionary[i] for i in score]
