class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.stack.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop == self.minimum:
            if self.stack:
                self.minimum = min(self.stack)
            else:
                self.minimum = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Alternative solution

class MinStack1:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum or self.minimum[-1] >= val:
            self.minimum.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
