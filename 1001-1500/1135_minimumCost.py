class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        self.parent[root_b] = root_a
        return True

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda x: x[2])
        uf = UnionFind(n)
        total_cost = 0

        for a, b, cost in connections:
            if uf.union(a - 1, b - 1):
                total_cost += cost

        root = uf.find(0)

        for i in range(1, n):
            if uf.find(i) != root:
                return -1

        return total_cost
