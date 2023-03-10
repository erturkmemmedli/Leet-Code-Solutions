class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.stack))):
            self.stack[i] += val
            
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

# Alternative solution

class CustomStack1:
    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        if len(self.stack) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.inc[min(k, len(self.stack)) - 1] += val
