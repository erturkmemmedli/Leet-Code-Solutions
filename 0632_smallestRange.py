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

# Alternative solution

class Solution1:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:      
        numsMerged = []
        for i, group in enumerate(nums):
            heapq.heappush(numsMerged, (group[0], i, 0))
        maxValue = max(group[0] for group in nums)
        left, right = 0, float('inf')
        while numsMerged:
            minValue, listIndex, numIndex = heapq.heappop(numsMerged)
            if maxValue - minValue < right - left:
                left, right = minValue, maxValue
            if numIndex + 1 == len(nums[listIndex]):
                return [left, right]
            candidate = nums[listIndex][numIndex + 1]
            maxValue = max(maxValue, candidate)
            heapq.heappush(numsMerged, (candidate, listIndex, numIndex + 1))
        
