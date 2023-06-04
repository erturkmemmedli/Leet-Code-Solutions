class Allocator:

    def __init__(self, n: int):
        self.memo = defaultdict(list)
        self.availability = [[0, n]]

    def allocate(self, size: int, mID: int) -> int:
        for i, [left, right] in enumerate(self.availability):
            if right - left >= size:
                if right - left >= size:
                    updated_interval = [left + size, right]
                    self.memo[mID].append([left, left + size])
                    self.availability[i] = updated_interval
                return left
        return -1

    def free(self, mID: int) -> int:
        if mID not in self.memo:
            return 0

        intervals = self.memo[mID]
        total = sum(r - l for l, r in intervals)

        for interval in intervals:
            self.merge(interval)

        del self.memo[mID]

        return total

    def merge(self, interval):
        left, right = interval

        if right < self.availability[0][0]:
            self.availability = [[left, right]] + self.availability
            return

        if right == self.availability[0][0]:
            self.availability[0][0] = left
            return

        if left > self.availability[-1][1]:
            self.availability += [[left, right]]
            return

        if left == self.availability[-1][1]:
            self.availability[-1][1] = right
            return

        final_result = []
        i = 0

        while i < len(self.availability):
            l, r = self.availability[i]
            if r < left:
                final_result.append([l, r])
                i += 1
            elif r == left:
                self.availability[i] = [l, right]

                if i + 1 < len(self.availability) and self.availability[i + 1][0] == right:
                    self.availability[i + 1] = [l, self.availability[i + 1][1]]
                    i += 1
                break
            elif l == right:
                self.availability[i] = [left, r]
                break
            else:
                final_result.append([left, right])
                break

        self.availability = final_result + self.availability[i:]


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
