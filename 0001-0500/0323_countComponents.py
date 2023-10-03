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

# Alternative solution

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.cc = n

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_b] < self.rank[root_a]:
                self.parent[root_b] = self.parent[root_a]
                self.rank[root_a] += self.rank[root_b]
            else:
                self.parent[root_a] = self.parent[root_b]
                self.rank[root_b] += self.rank[root_a]
            self.cc -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)

        return uf.cc

# Alternative solution

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph = collections.defaultdict(list)

        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)

        self.visited = set()
        connected_components = 0

        for i in range(n):
            if i not in self.visited:
                self.dfs(i)
                connected_components += 1

        return connected_components
            
    def dfs(self, node):
        self.visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
