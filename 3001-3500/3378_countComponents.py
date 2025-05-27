class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        elif self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.rank[ra] += 1
            self.parent[rb] = ra


class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        uf = UnionFind(threshold + 1)
        parent_map = defaultdict(int)
        nums.sort()

        for num in nums:
            for j in range(num, threshold + 1, num):
                if self.lcm(num, j) <= threshold:
                    uf.union(num, j)

        i = 0 
        while i < len(nums):
            if nums[i] <= threshold:
                parent_map[uf.find(nums[i])] += 1
                i += 1
            else:
                break
        
        print(parent_map)
        return len(parent_map) + len(nums) - i
    
    def lcm(self, a, b):
        gcd = self.gcd(a, b)
        return a * b // gcd

    def gcd(self, a, b):
        while a % b != 0:
            a, b = b, a % b
        return b
