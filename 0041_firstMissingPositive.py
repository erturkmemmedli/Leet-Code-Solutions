import heapq

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        start = 1
        while nums:
            pop = heapq.heappop(nums)
            if pop < start:
                continue
            elif pop > start:
                return start
            else: 
                start += 1
        if pop < 0: 
            return 1
        else: 
            return pop + 1
