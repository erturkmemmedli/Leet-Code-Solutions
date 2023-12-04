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

# Alternative solution

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        right_intervals = [-1 for i in range(len(intervals))]
        start_heap = []
        end_heap = []

        for i, [start, end] in enumerate(intervals):
            heappush(start_heap, (start, i))
            heappush(end_heap, (end, i))

        while start_heap and end_heap:
            if start_heap[0][0] < end_heap[0][0]:
                heappop(start_heap)
            else:
                _, index = heappop(end_heap)
                right_intervals[index] = start_heap[0][1]

        return right_intervals

# Alternative solution

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted([(start, end, index) for index, [start, end] in enumerate(intervals)])
        heap = []
        right_intervals = [-1] * len(intervals)

        for start, end, index in intervals:
            if start == end:
                right_intervals[index] = index
                continue
                
            while heap and start >= heap[0][0]:
                e, i = heappop(heap)
                right_intervals[i] = index
            
            heappush(heap, (end, index))

        return right_intervals
