from sortedcontainers import SortedList

class MedianFinder:
    def __init__(self):
        self.dataStream = SortedList()

    def addNum(self, num: int) -> None:
        self.dataStream.add(num)

    def findMedian(self) -> float:
        n = len(self.dataStream)
        if n % 2:
            return self.dataStream[n // 2]
        return (self.dataStream[n // 2 - 1] + self.dataStream[n // 2]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Alternative solution

class MedianFinder1:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (self.minHeap[0] - self.maxHeap[0]) / 2
