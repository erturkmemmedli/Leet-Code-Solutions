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
            return

        self.parent[root_b] = root_a

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if self.similar(strs[i], strs[j]):
                    uf.union(i, j)
                
        connected_components = 0

        for i in range(n):
            if i == uf.parent[i]:
                connected_components += 1
            
        return connected_components

    def similar(self, x, y):
        indices = []

        for i in range(len(x)):
            if x[i] != y[i]:
                indices.append(i)

            if len(indices) > 2:
                return False

        return True
