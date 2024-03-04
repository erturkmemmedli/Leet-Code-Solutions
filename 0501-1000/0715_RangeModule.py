class RangeModule:
    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
        self.track[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
        self.track[start:end] = subtrack

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# Alternative solution

from sortedcontainers import SortedList

class RangeModule:
    def __init__(self):
        self.track = SortedList()

    def addRange(self, left: int, right: int) -> None:
        start = self.track.bisect_left(left)
        end = self.track.bisect_right(right)
        for _ in range(start, end):
            # because each time we pop same index when we pop starting index
            self.track.pop(start)
        if start % 2 == 0: self.track.add(left)
        if end % 2 == 0: self.track.add(right)

    def queryRange(self, left: int, right: int) -> bool:
        start = self.track.bisect_right(left)
        end = self.track.bisect_left(right)
        return start == end and start % 2

    def removeRange(self, left: int, right: int) -> None:
        start = self.track.bisect_left(left)
        end = self.track.bisect_right(right)
        for _ in range(start, end):
            # because each time we pop same index when we pop starting index
            self.track.pop(start)
        if start % 2 == 1: self.track.add(left)
        if end % 2 == 1: self.track.add(right) 
