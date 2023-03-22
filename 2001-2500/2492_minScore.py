class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
            
        return a
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return
        
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        
        elif self.rank[root_b] < self.rank[root_a]:
            self.parent[root_b] = root_a
            
        else:
            self.rank[root_a] += 1
            self.parent[root_b] = root_a

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for a, b, dist in roads:
            uf.union(a - 1, b - 1)

        minimum_path = float("inf")
        
        for a, b, dist in roads:
            if uf.find(0) == uf.find(a - 1):
                minimum_path = min(minimum_path, dist)
                
        return minimum_path
        
# Alternative solution (which gives TLE error)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))
            
        queue = deque([(1, float("inf"))])
        visited = {1}
        minimum_path = float("inf")
        
        while queue:
            node, distance = queue.popleft()
            minimum_path = min(minimum_path, distance)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return minimum_path
