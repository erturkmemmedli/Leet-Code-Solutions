from sortedcontainers import SortedList
from bisect import bisect_left

class MyCalendar:
    def __init__(self):
        self.list = SortedList()

    def book(self, start: int, end: int) -> bool:
        if not self.list:
            self.list.add([start, end])
            return True
        index = bisect_left(self.list, [start, end])
        if index == 0:
            if end > self.list[0][0]:
                return False
            else:
                self.list.add([start, end])
                return True
        elif index == len(self.list):
            if start < self.list[-1][1]:
                return False
            else:
                self.list.add([start, end])
                return True
        else:
            if start < self.list[index - 1][1] or end > self.list[index][0]:
                return False
            else:
                self.list.add([start, end])
                return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
