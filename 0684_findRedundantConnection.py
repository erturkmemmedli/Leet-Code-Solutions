from collections import defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            if self.bfs(a, b, graph, set()):
                return [a, b]
            graph[a].append(b)
            graph[b].append(a)
            
    def bfs(self, node, parent, graph, visited):
        queue = deque()
        queue.append(node)
        visited.add(node)
        while queue:
            node = queue.popleft()
            if node == parent:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(node)

# Alternative solution                    
                    
from collections import defaultdict

class Solution1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            if self.dfs(a, b, graph, set()):
                return [a, b]
            graph[a].append(b)
            graph[b].append(a)
            
    def dfs(self, node, parent, graph, visited):
        if node not in visited:
            visited.add(node)
            if node == parent:
                return True
            for neighbor in graph[node]:
                if self.dfs(neighbor, parent, graph, visited):
                    return True
                  
# Alternative solution

class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parent = [-1] * (n+1)
        self.rank = [0] * (n+1)
        for a, b in edges:
            if not self.union(a, b):
                return [a, b]
        
    def find(self, x):
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        elif root_a < root_b:
            self.parent[root_a] = root_b
            self.rank[root_b] += 1
            return True
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
            return True
          
# Alternative solution

class Solution3:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.parent = [i for i in range(n)]
        self.rank = [i for i in range(n)]
        for a, b in edges:
            if not self.union(a-1, b-1):
                return [a, b]
                
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            x =  self.parent[x]
        return x
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        elif root_a < root_b:
            self.parent[root_a] = root_b
            self.rank[root_b] += self.rank[root_a]
            return True
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += self.rank[root_b]
            return True
