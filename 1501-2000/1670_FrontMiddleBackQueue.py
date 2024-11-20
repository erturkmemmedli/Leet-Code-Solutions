from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.left_queue = deque()
        self.right_queue = deque()

    def pushFront(self, val: int) -> None:
        self.left_queue.appendleft(val)
        if len(self.left_queue) > len(self.right_queue):
            self.right_queue.appendleft(self.left_queue.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.left_queue) == len(self.right_queue):
            self.right_queue.appendleft(val)
        else:
            self.left_queue.append(val)

    def pushBack(self, val: int) -> None:
        self.right_queue.append(val)
        if len(self.left_queue) + 1 < len(self.right_queue):
            self.left_queue.append(self.right_queue.popleft())

    def popFront(self) -> int:
        if not self.left_queue and not self.right_queue:
            return -1
        elif not self.left_queue:
            return self.right_queue.pop()
        val = self.left_queue.popleft()
        if len(self.left_queue) + 1 < len(self.right_queue):
            self.left_queue.append(self.right_queue.popleft())
        return val

    def popMiddle(self) -> int:
        if not self.left_queue and not self.right_queue:
            return -1
        elif not self.left_queue:
            return self.right_queue.pop()
        if len(self.left_queue) == len(self.right_queue):
            val = self.left_queue.pop()
            return val
        else:
            val = self.right_queue.popleft()
            return val

    def popBack(self) -> int:
        if not self.left_queue and not self.right_queue:
            return -1
        elif not self.left_queue:
            return self.right_queue.pop()
        val = self.right_queue.pop()
        if len(self.left_queue) > len(self.right_queue):
            self.right_queue.appendleft(self.left_queue.pop())
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
