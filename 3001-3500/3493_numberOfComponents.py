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
            self.parent[rb] = ra
            self.rank[ra] += 1


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        uf = UnionFind(n)
        properties = [set(prop) for prop in properties]

        for i in range(n):
            for j in range(i + 1, n):
                if len(properties[i] & properties[j]) >= k:
                    uf.union(i, j)

        result = set()
        for i in range(n):
            result.add(uf.find(i))

        return len(result)
