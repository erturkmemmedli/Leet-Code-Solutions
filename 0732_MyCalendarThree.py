from sortedcontainers import SortedDict

class MyCalendarThree:
    def __init__(self):
        self.path = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.path[startTime] = self.path.get(startTime, 0) + 1
        self.path[endTime] = self.path.get(endTime, 0) - 1
        current = 0
        result = 0
        for val in self.path.values():
            current += val
            result = max(result, current)
        return result

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

# Alternative solution

class MyCalendarThree1:
    def __init__(self):
        self.segment = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.updateSegmentTreeWithLazyPropagation(startTime, endTime - 1)
        return self.segment[1]

    def updateSegmentTreeWithLazyPropagation(self, start, end, left = 0, right = 10 ** 9, index = 1):
        if right < start or left > end:
            return
        if start <= right <= left <= end:
            self.segment[index] += 1
            self.lazy[index] += 1
        else:
            mid = (left + right) // 2
            self.updateSegmentTreeWithLazyPropagation(start, end, left, mid, 2 * index)
            self.updateSegmentTreeWithLazyPropagation(start, end, mid + 1, right, 2 * index + 1)
            self.segment[index] = self.lazy[index] + max(self.segment[2 * index], self.segment[2 * index + 1])
