class Router:

    def __init__(self, memoryLimit: int):
        self.max_size = memoryLimit
        self.packet_cache = set()
        self.destination_map = defaultdict(list)
        self.queue = deque()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, source, destination) in self.packet_cache:
            return False
        
        if len(self.queue) == self.max_size:
            t, s, d = self.queue.popleft()
            self.packet_cache.remove((t, s, d))
            self.destination_map[d].pop(0)

        self.packet_cache.add((timestamp, source, destination))
        self.queue.append([timestamp, source, destination])
        self.destination_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.queue) == 0:
            return []

        t, s, d = self.queue.popleft()
        self.packet_cache.remove((t, s, d))
        self.destination_map[d].pop(0)
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        dest = self.destination_map[destination]
        left = bisect_left(dest, startTime)
        right = bisect_right(dest, endTime)
        
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

# Alternative solution (TLE error)

class Router:

    def __init__(self, memoryLimit: int):
        self.max_size = memoryLimit
        self.packet_cache = set()
        self.list = []
        self.idx = 0

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, source, destination) in self.packet_cache:
            return False
        
        if len(self.list) - self.idx == self.max_size:
            self.packet_cache.remove(tuple(self.list[self.idx]))
            self.idx += 1

        self.packet_cache.add((timestamp, source, destination))
        self.list.append([timestamp, source, destination])
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.list) - self.idx == 0:
            return []

        self.packet_cache.remove(tuple(self.list[self.idx]))
        t, s, d = self.list[self.idx]
        self.idx += 1
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        low, high = self.idx, len(self.list)
        left = bisect_left(self.list, startTime, low, high, key=itemgetter(0))
        right = bisect_right(self.list, endTime, low, high, key=itemgetter(0))
        
        if right == len(self.list) or (right < len(self.list) and self.list[right][0] > endTime):
            right -= 1

        count = 0

        for i in range(left, right+1):
            if 0 <= i < len(self.list) and self.list[i][2] == destination:
                count += 1
        
        return count
