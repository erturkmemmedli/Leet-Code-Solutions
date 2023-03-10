class FreqStack:
    def __init__(self):
        self.stack = []
        self.hashmap = {}

    def push(self, val: int) -> None:
        if val not in self.hashmap:
            self.hashmap[val] = 1
        else:
            self.hashmap[val] += 1
        if len(self.stack) < self.hashmap[val]:
            self.stack.append([])
        self.stack[self.hashmap[val] - 1].append(val)

    def pop(self) -> int:
        pop = self.stack[-1].pop()
        self.hashmap[pop] -= 1
        if len(self.stack[-1]) == 0:
            self.stack.pop()
        return pop

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
