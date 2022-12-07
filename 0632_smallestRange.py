class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minimumDistance = float('inf')
        minimumDistancePair = None        
        numsMerged = []
        for i, group in enumerate(nums):
            for num in group:
                heapq.heappush(numsMerged, (num, i))
        window = {}
        while numsMerged:
            num, group = heapq.heappop(numsMerged)
            window[group] = num
            minWindow = min(window.values())
            maxWindow = max(window.values())
            if len(window) == len(nums):
                if maxWindow - minWindow < minimumDistance:
                    minimumDistance = maxWindow - minWindow
                    minimumDistancePair = [minWindow, maxWindow]
        return minimumDistancePair
