class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.availableFirst = {}
        self.availableLast = {}
        self.heap = []
        self.addSegment(0, n - 1)

    def addSegment(self, first, last):
        if first == 0 or last == self.n - 1:
            priority = last - first
        else:
            priority = (last - first) // 2
        segment = [-priority, first, last, True]
        self.availableFirst[first] = segment
        self.availableLast[last] = segment
        heapq.heappush(self.heap, segment)

    def seat(self) -> int:
        while True:
            priority, first, last, isValid = heapq.heappop(self.heap)
            if isValid:
                del self.availableFirst[first]
                del self.availableLast[last]
                break
        if first == 0:
            temp = first
            if first != last:
                self.addSegment(first + 1, last)
        elif last == self.n - 1:
            temp = last
            if first != last:
                self.addSegment(first, last - 1)
        else:
            temp = first - priority
            if temp > first:
                self.addSegment(first, temp - 1)
            if temp < last:
                self.addSegment(temp + 1, last)
        return temp

    def leave(self, p: int) -> None:
        first = p
        last = p
        left = p - 1
        right = p + 1
        if left >= 0 and left in self.availableLast:
            segmentLeft = self.availableLast.pop(left)
            segmentLeft[3] = False
            first = segmentLeft[1]
        if right < self.n and right in self.availableFirst:
            segmentRight = self.availableFirst.pop(right)
            segmentRight[3] = False
            last = segmentRight[2]
        self.addSegment(first, last)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
