class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        minHeap = []
        maxHeap = []
        medians = []

        irrelevant = {num : 0 for num in nums}
        i = 0

        while i < k:
            if not maxHeap or -maxHeap[0] > nums[i]:
                heapq.heappush(maxHeap, -nums[i])
            else:
                heapq.heappush(minHeap, nums[i])

            if len(maxHeap) > len(minHeap) + 1:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            if len(minHeap) > len(maxHeap):
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))

            i += 1
        
        while True:
            medians.append(-maxHeap[0] if k % 2 == 1 else (minHeap[0] - maxHeap[0]) / 2)

            if i == len(nums):
                break

            remove = nums[i - k]
            add = nums[i]
            
            irrelevant[remove] += 1
            balance = 0

            if not maxHeap or remove <= -maxHeap[0]:
                balance -= 1
            else:
                balance += 1

            if add <= -maxHeap[0]:
                balance += 1
                heapq.heappush(maxHeap, -add)
            else:
                balance -= 1
                heapq.heappush(minHeap, add)

            if balance > 0:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            if balance < 0:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))

            while maxHeap and irrelevant[-maxHeap[0]] > 0:
                irrelevant[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)

            while minHeap and irrelevant[minHeap[0]] > 0:
                irrelevant[minHeap[0]] -= 1
                heapq.heappop(minHeap)

            i += 1

        return medians

# Alternative solution

from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        answer = []

        for i in range(k):
            window.add(nums[i])

        answer.append(window[k//2] if k & 1 else( window[k//2 - 1] + window[k//2]) / 2)

        for i in range(k, len(nums)):
            window.remove(nums[i-k])
            window.add(nums[i])
            answer.append(window[k//2] if k & 1 else( window[k//2 - 1] + window[k//2]) / 2)
        
        return answer
