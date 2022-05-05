from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)
        return

    def pop(self) -> int:
        popped = self.queue.popleft()
        return popped

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return self.queue == deque([])

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
