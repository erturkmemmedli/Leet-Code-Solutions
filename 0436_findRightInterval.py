class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startHeap = []
        endHeap = []
        rightIntervals = [-1 for _ in range(len(intervals))]
        for i, [a, b] in enumerate(intervals):
            heapq.heappush(startHeap, (a, i))
            heapq.heappush(endHeap, (b, i))
        for _ in range(len(intervals)):
            left, leftIndex = heapq.heappop(startHeap)
            while endHeap and left >= endHeap[0][0]:
                right, rightIndex = heapq.heappop(endHeap)
                rightIntervals[rightIndex] = leftIndex
        return rightIntervals
        
# Alternative solution

class Solution1:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted([[a,b,i] for i, [a,b] in enumerate(intervals)])
        answer = [-1 for _ in range(len(intervals))]
        starts = [a for a, _, _ in intervals]
        for a, b, i in intervals:
            index = bisect.bisect_left(starts, b)
            if index < len(intervals):
                answer[i] = intervals[index][2]
        return answer
