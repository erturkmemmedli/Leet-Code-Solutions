class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        heapq.heapify(nums)
        while nums:
            pop = heapq.heappop(nums)
            if pop >= 0:
                return -1
            if -pop in s:
                return -pop
        return -1
