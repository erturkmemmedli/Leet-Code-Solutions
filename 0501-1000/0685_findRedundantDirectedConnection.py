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
            return False
        
        self.parent[root_b] = root_a
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = {i : 0 for i in range(n)}
        uf = UnionFind(n)

        # check whether there is node with 2 parents
        for a, b in edges:
            indegree[b - 1] += 1

        # if there is not 2 parents, simple union-find algorithm will work
        if max(indegree.values()) == 1:
            for a, b in edges:
                if not uf.union(a - 1, b - 1):
                    return [a, b]

        # otherwise, we need to check the specific node with 2 parents
        else:
            # we determine the node with 2 parents
            node = [key for key, val in indegree.items() if val == 2][0] + 1
            problematic_edges = []

            # we determine at wich indices we this node is destionation point
            for i, [a, b] in enumerate(edges):
                if b == node:
                    problematic_edges.append(i)

            # we connect other edges by union-find algorithm except edges including this node in destination side
            for i, [a, b] in enumerate(edges):
                if i not in problematic_edges:
                    uf.union(a - 1, b - 1)

            # since 2 edges left, we find the problematic edge that occurs last in the input
            result = None

            for i in problematic_edges:
                a, b = edges[i]
                if not uf.union(a - 1, b - 1):
                    result = [a, b]

            return result

# Alternative solution

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
    
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            if self.rank[ra] < self.rank[rb]:
                self.parent[ra] = rb
            elif self.rank[ra] == self.rank[rb]:
                self.parent[rb] = ra
                self.rank[ra] += 1
            else:
                self.parent[rb] = ra
            return True
        return False

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegree = {i : [] for i in range(n)}

        problems = []

        for a, b in edges:
            indegree[b - 1].append([a, b])
            if len(indegree[b - 1]) == 2:
                problems.extend(indegree[b - 1])
                break

        uf = UnionFind(n)

        for a, b in edges:
            if [a, b] not in problems:
                if not uf.union(a - 1, b - 1):
                    return [a, b]

        for a, b in problems:
            if not uf.union(a - 1, b - 1):
                return [a, b]
