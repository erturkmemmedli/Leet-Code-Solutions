class SnapshotArray:
    def __init__(self, length: int):
        self.snapArray = collections.defaultdict(list)
        self.snapTime = 0

    def set(self, index: int, val: int) -> None:
        if self.snapArray[index] and self.snapArray[index][-1][0] == self.snapTime:
            self.snapArray[index][-1][1] = val
        else:
            self.snapArray[index].append([self.snapTime, val])

    def snap(self) -> int:
        self.snapTime += 1
        return self.snapTime - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.snapArray[index]
        left, right, idx = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                idx = mid
                left = mid + 1
            else:
                right = mid - 1
        return 0 if idx == -1 else arr[idx][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# Alternative solution (which gives TLE error)

class SnapshotArray1:
    def __init__(self, length: int):
        self.snapArray = {i: [[-1, 0]] for i in range(length)}
        self.snapTime = 0

    def set(self, index: int, val: int) -> None:
        self.snapArray[index][-1][1] = val
        
    def snap(self) -> int:
        self.snapTime += 1
        for i in range(len(self.snapArray)):
            snapIndex, snapValue = self.snapArray[i][-1]
            self.snapArray[i].append([snapIndex + 1, snapValue])
        return self.snapTime - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect.bisect_left(self.snapArray[index], [snap_id, 0])
        return self.snapArray[index][idx - 1][1]
