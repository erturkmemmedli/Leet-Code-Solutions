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
        self.updateSegmentTreeWithLazyPropagation(startTime, endTime)
        return self.segment[1]

    def updateSegmentTreeWithLazyPropagation(self, start, end, left = 0, right = 10 ** 9, index = 1):
        if right <= start or left >= end:
            return
        if start <= left < right <= end:
            self.segment[index] += 1
            self.lazy[index] += 1
        else:
            mid = (left + right) // 2
            self.updateSegmentTreeWithLazyPropagation(start, end, left, mid, 2 * index)
            self.updateSegmentTreeWithLazyPropagation(start, end, mid, right, 2 * index + 1)
            self.segment[index] = self.lazy[index] + max(self.segment[2 * index], self.segment[2 * index + 1])

# Alternative solution

from sortedcontainers import SortedList

class MyCalendarThree2:
    def __init__(self):
        self.list = SortedList([[0, 0]])
        self.result = 0

    def book(self, startTime: int, endTime: int) -> int:
        self.construct(startTime)
        self.construct(endTime)
        for interval in self.list.irange([startTime, 0], [endTime, 0], inclusive = (True, False)):
            interval[1] += 1
            self.result = max(self.result, interval[1])
        return self.result

    def construct(self, new):
        index = bisect.bisect_left(self.list, [new, 0])
        if index < len(self.list) and self.list[index][0] == new:
            return
        self.list.add([new, self.list[index - 1][1]])

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
