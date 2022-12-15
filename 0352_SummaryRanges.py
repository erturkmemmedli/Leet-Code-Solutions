from sortedcontainers import SortedList
from bisect import bisect_left

class SummaryRanges:
    def __init__(self):
        self.intervals = SortedList()

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.add([value, value])
        else:
            index = bisect_left(self.intervals, [value, value])
            if index == 0:
                if value == self.intervals[0][0]:
                    pass
                elif value == self.intervals[0][0] - 1:
                    self.intervals[0][0] -= 1
                else:
                    self.intervals.add([value, value])
            elif index == len(self.intervals):
                if value <= self.intervals[-1][1]:
                    pass
                elif value == self.intervals[-1][1] + 1:
                    self.intervals[-1][1] += 1
                else:
                    self.intervals.add([value, value])
            else:
                if value <= self.intervals[index-1][1] or value == self.intervals[index][0]:
                    pass
                elif self.intervals[index-1][1] + 1 == value == self.intervals[index][0] - 1:
                    right = self.intervals.pop(index)
                    left = self.intervals.pop(index-1)
                    self.intervals.add([left[0], right[1]])
                elif value == self.intervals[index-1][1] + 1:
                    self.intervals[index-1][1] += 1
                elif value == self.intervals[index][0] - 1:
                    self.intervals[index][0] -= 1
                else:
                    self.intervals.add([value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
