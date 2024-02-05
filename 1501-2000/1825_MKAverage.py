from collections import deque
from sortedcontainers import SortedList

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k= k
        self.nums = deque()
        self.stream = SortedList()

    def addElement(self, num: int) -> None:
        if len(self.nums) >= self.m:
            head = self.nums.popleft()
            self.stream.remove(head)
        self.nums.append(num)
        self.stream.add(num)

    def calculateMKAverage(self) -> int:
        k = self.k
        m = self.m
        return sum(self.stream[k:m-k])//(m-2*k) if len(self.nums) == m else -1         


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
