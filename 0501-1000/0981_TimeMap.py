class TimeMap:
    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [[timestamp, value]]
        else:
            self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        index = bisect.bisect_left(self.hashmap[key], timestamp, key = lambda x: x[0])
        if index < len(self.hashmap[key]):
            if timestamp == self.hashmap[key][index][0]:
                return self.hashmap[key][index][1]
            elif index == 0:
                return ""
            else:
                return self.hashmap[key][index - 1][1]
        else:
            return self.hashmap[key][-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
