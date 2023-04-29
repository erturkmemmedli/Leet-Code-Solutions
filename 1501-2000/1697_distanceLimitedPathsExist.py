class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        self.parent[root_b] = root_a

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList = sorted(edgeList, key = lambda x: x[2])
        queries = sorted((w, u, v, i) for i, (u, v, w) in enumerate(queries))
        uf = UnionFind(n)
        answer = [None for _ in range(len(queries))]
        i = 0
        for limit, u, v, idx in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                a, b, w = edgeList[i]
                uf.union(a, b)
                i += 1
            answer[idx] = uf.find(u) == uf.find(v)
        return answer
