class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a
            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        roots = 0
        for i in range(n):
            if i == uf.parent[i]:
                roots += 1
        return roots
