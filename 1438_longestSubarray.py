class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeap, minHeap = [], []
        maxLength, index = 0, 0
        for i, num in enumerate(nums):
            heapq.heappush(maxHeap, [-num, i])
            heapq.heappush(minHeap, [num, i])
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                index = min(maxHeap[0][1], minHeap[0][1]) + 1
                while maxHeap[0][1] < index: heapq.heappop(maxHeap)
                while minHeap[0][1] < index: heapq.heappop(minHeap)
            maxLength = max(maxLength, i - index + 1)
        return maxLength
        
# Alternative solution

from collections import deque

class Solution1:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQueue, minQueue = deque(), deque()
        i = 0
        for num in nums:
            while maxQueue and num > maxQueue[-1]: maxQueue.pop()
            while minQueue and num < minQueue[-1]: minQueue.pop()
            maxQueue.append(num)
            minQueue.append(num)
            if maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                i += 1
        return len(nums) - i
