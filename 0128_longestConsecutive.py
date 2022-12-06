class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        self.parent = {num : num for num in nums}
        self.rank = {num: 0 for num in nums}
        for num in nums:
            self.union(num, num - 1)
            self.union(num, num + 1)
        for num in nums:
            self.find(num)
        return max(val for val in collections.Counter(self.parent.values()).values())
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        if a in self.parent and b in self.parent:
            da, db = self.find(a), self.find(b)
            if da == db:
                return
            elif self.rank[da] < self.rank[db]:
                self.parent[da] = db
            else:
                if self.rank[da] > self.rank[db]:
                    self.parent[db] = da
                else:
                    self.parent[db] = da
                    self.rank[da] += 1
