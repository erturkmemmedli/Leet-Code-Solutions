class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        result = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                visited.add(i)
                temp = [i]
                self.dfs(isConnected, n, i, visited, temp)
                result += 1
        return result
        
    def dfs(self, isConnected, n, i, visited, temp):
        for j in range(n):
            if isConnected[i][j] == 1 and j not in visited:
                visited.add(j)
                temp.append(j)
                self.dfs(isConnected, n, j, visited, temp)
                
# Alternative solution

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

        if root_a != root_b:
            self.parent[root_b] = root_a

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        
        for i in range(n):
            uf.parent[i] = uf.find(uf.parent[i])

        return len(set(uf.parent))
