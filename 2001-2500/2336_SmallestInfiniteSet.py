class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = [1]
        self.checker = set()

    def popSmallest(self) -> int:
        val = heapq.heappop(self.smallest)
        self.checker.add(val)
        if not self.smallest:
            heapq.heappush(self.smallest, val + 1)
        return val

    def addBack(self, num: int) -> None:
        if num in self.checker:
            self.checker.remove(num)
            heapq.heappush(self.smallest, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
