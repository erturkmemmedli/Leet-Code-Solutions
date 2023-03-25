class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, a):
        if a != self.parent[a]:
            a = self.find(self.parent[a])
    
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b

        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
            
        else:
            self.rank[root_a] += 1
            self.parent[root_b] = root_a
 
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)
            
        connected_components = collections.defaultdict(int)

        for i in range(n):
            connected_components[uf.find(i)] += 1

        components = list(connected_components.values())
        unreachables = 0
        multiplication_factor = components[0]

        for i in range(1, len(components)):
            unreachables += components[i] * multiplication_factor
            multiplication_factor += components[i]
            
        return unreachables
      
# Alternative solution

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.graph = collections.defaultdict(list)
        self.visited = set()
        self.connected_components = [None] * n
        self.rank = 0

        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)

        for i in range(n):
            if i not in self.visited:
                self.dfs(i)
                self.rank += 1

        component_density = list(Counter(self.connected_components).values())
        factor = component_density[0]
        answer = 0

        for i in range(1, len(component_density)):
            answer += component_density[i] * factor
            factor += component_density[i]

        return answer

    def dfs(self, node):
        if node not in self.visited:
            self.visited.add(node)
            self.connected_components[node] = self.rank

            for neighbor in self.graph[node]:
                self.dfs(neighbor)

# Alternative solution (which gives TLE error)

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, a):
        if a != self.parent[a]:
            a = self.find(self.parent[a])
    
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b

        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
            
        else:
            self.rank[root_a] += 1
            self.parent[root_b] = root_a
 
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)
            
        connected_components = collections.defaultdict(int)

        for i in range(n):
            connected_components[uf.find(i)] += 1

        components = list(connected_components.values())
        unreachables = 0

        for i in range(len(components)):
            for j in range(i + 1, len(components)):
                unreachables += components[i] * components[j]
            
        return unreachables
