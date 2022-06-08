from collections import deque

class RecentCounter:
    def __init__(self):
        self.counter = 0
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue:
            if t - 3000 > self.queue[0]:
                self.queue.popleft()
            else:
                break
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
