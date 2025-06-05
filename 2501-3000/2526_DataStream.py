class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.counter = {}
        self.window = deque()

    def consec(self, num: int) -> bool:
        self.window.append(num)
        self.counter[num] = self.counter.get(num, 0) + 1

        if len(self.window) > self.k:
            val = self.window.popleft()
            self.counter[val] -= 1
            if self.counter[val] == 0:
                del self.counter[val]
        
        if len(self.window) < self.k:
            return False
        
        if len(self.counter) > 1:
            return False

        return self.value in self.counter


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
