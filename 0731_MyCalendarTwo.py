class MyCalendarTwo:
    def __init__(self):
        self.firstEvent = set()
        self.secondEvent = set()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.secondEvent:
            if s < start < e or s < end < e or (start <= s and end >= e):
                return False
        for s, e in self.firstEvent:
            if e <= start or end <= s:
                continue
            self.secondEvent.add((max(start, s), min(end, e)))
        self.firstEvent.add((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
