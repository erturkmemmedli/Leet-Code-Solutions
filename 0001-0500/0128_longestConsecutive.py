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

# Alternative solution

class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        self.parent = {num : num for num in nums}
        self.rank = {num: 1 for num in nums}
        for num in nums:
            self.union(num, num - 1)
            self.union(num, num + 1)
        for num in nums:
            self.find(num)
        return max(self.rank.values(), default = 0)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        if a in self.parent and b in self.parent:
            da, db = self.find(a), self.find(b)
            if da == db:
                return
            if self.rank[da] < self.rank[db]:
                self.parent[da] = db
                self.rank[db] += self.rank[da]
            else:
                self.parent[db] = da
                self.rank[da] += self.rank[db]
