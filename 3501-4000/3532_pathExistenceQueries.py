class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node
    
    def union(self, nodeA, nodeB):
        rootA = self.find(nodeA)
        rootB = self.find(nodeB)

        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.rank[rootA] += 1
            self.parent[rootB] = rootA        


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] <= maxDiff:
                uf.union(i, i - 1)
        
        return [uf.find(u) == uf.find(v) for u, v in queries]
