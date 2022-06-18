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

# Alternative solution

class MyQueue1:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        popped = self.queue[0] 
        self.queue = self.queue[1:]
        return popped

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not len(self.queue)

# Alternative solution

class MyQueue2:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, x: int) -> None:
        self.stackIn.append(x)

    def pop(self) -> int:
        self.transport()
        return self.stackOut.pop()

    def peek(self) -> int:
        self.transport()
        return self.stackOut[-1]

    def empty(self) -> bool:
        return not self.stackIn and not self.stackOut
        
    def transport(self):
        if not self.stackOut:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop())
