class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.removed = set()
        self.existing = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            if val in self.removed:
                self.removed.remove(val)
            self.existing.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            self.removed.add(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.existing) - 1)
        while self.existing[idx] in self.removed:
            idx = random.randint(0, len(self.existing) - 1)
        return self.existing[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Alternative solution

class RandomizedSet1:
    def __init__(self):
        self.hashmap = {}
        self.existing = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.hashmap[val] = self.count
            self.existing[self.count] = val
            self.count += 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        else:
            idx = self.hashmap.pop(val)
            self.existing.pop(idx)
            if idx != self.count - 1:
                val = self.existing.pop(self.count - 1)
                self.hashmap[val] = idx
                self.existing[idx] = val
            self.count -= 1
            return True

    def getRandom(self) -> int:
        index = random.randint(0, self.count - 1)
        return self.existing[index]
