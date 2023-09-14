class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        
    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
            
        return node
        
    def union(self, nodeA, nodeB):
        rootA = self.find(nodeA)
        rootB = self.find(nodeB)
        
        if rootA == rootB:
            return False
            
        self.parent[rootB] = rootA
        
        return True
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        uf = UnionFind(n)
        
        for a, b in edges:
            if not uf.union(a, b):
                return False
        
        return True
