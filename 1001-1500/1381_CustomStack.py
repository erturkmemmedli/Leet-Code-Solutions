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

# Alternative solution

class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if self.capacity:
            self.stack.append([x, 0])
            self.capacity -= 1

    def pop(self) -> int:
        if not self.stack:
            return -1
        pop = self.stack.pop()
        self.capacity += 1
        if self.stack:
            self.stack[-1][1] += pop[1]
        return sum(pop)

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.stack[min(len(self.stack) - 1, k - 1)][1] += val

# Alternative solution

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        self.heap = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        heap_val = 0
        if self.heap:
            heap_idx = -self.heap[0][0]
            if heap_idx == len(self.stack):
                while self.heap and self.heap[0][0] == -heap_idx:
                    heap_val += heappop(self.heap)[1]
                if self.heap and self.heap[0][0] - 1 == -heap_idx:
                    self.heap[0][1] += heap_val
                else:
                    heappush(self.heap, [-heap_idx + 1, heap_val])

        val = self.stack.pop() + heap_val
        return val

    def increment(self, k: int, val: int) -> None:
        heappush(self.heap, [max(-k, -len(self.stack)), val])
