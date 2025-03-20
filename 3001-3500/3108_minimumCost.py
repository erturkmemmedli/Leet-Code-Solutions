class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.cost = [-1] * n

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
    
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.rank[ra] += 1
            self.parent[rb] = ra


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        answer = [-1] * len(query)

        for a, b, c in edges:
            uf.union(a, b)

        for a, b, c in edges:
            ra = uf.find(a)
            uf.cost[ra] &= c
        
        for i, [a, b] in enumerate(query):
            ra = uf.find(a)
            rb = uf.find(b)
            if ra == rb:
                answer[i] = uf.cost[ra]
        
        return answer
