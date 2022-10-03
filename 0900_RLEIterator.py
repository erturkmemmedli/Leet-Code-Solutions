class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = collections.deque(encoding)

    def next(self, n: int) -> int:
        if not self.encoding:
            return -1
        if n < self.encoding[0]:
            self.encoding[0] -= n
            return self.encoding[1]
        elif n == self.encoding[0]:
            self.encoding.popleft()
            return self.encoding.popleft()
        else:
            n -= self.encoding.popleft()
            self.encoding.popleft()
            return self.next(n)

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
