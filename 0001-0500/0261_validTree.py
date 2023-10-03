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

# Alternative solution

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.cc = n

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a
            self.cc -= 1
            return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for node1, node2 in edges:
            if not uf.union(node1, node2):
                return False        

        return uf.cc == 1
        
        return True
