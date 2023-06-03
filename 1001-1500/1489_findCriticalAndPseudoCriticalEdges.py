class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
            
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b

        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a

        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
        
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(a, b, weight, idx) for idx, [a, b, weight] in enumerate(edges)]
        edges.sort(key = lambda x: x[2])
        base_weight = self.find_MST_without_this_edge(edges, n, -1)
        critical_indices = set()
        pseudo_critical_indices = set()

        for i in range(len(edges)):
            weight_excluded = self.find_MST_without_this_edge(edges, n, i)

            if weight_excluded > base_weight:
                critical_indices.add(edges[i][3])

            else:
                weight_included = self.find_MST_with_this_edge(edges, n, i)

                if weight_included == base_weight:
                    pseudo_critical_indices.add(edges[i][3])

        return [critical_indices, pseudo_critical_indices]

    def find_MST_without_this_edge(self, edges, n, edge_idx):
        uf = UnionFind(n)
        answer = 0

        for i, [a, b, weight, _] in enumerate(edges):
            if i == edge_idx:
                continue

            if uf.union(a, b):
                answer += weight
            
        parent = uf.find(0)

        return answer if all(uf.find(i) == parent for i in range(n)) else float('inf')

    def find_MST_with_this_edge(self, edges, n, edge_idx):
        uf = UnionFind(n)
        a0, b0, w0, _ = edges[edge_idx]
        answer = w0
        uf.union(a0, b0)

        for i, [a, b, weight, _] in enumerate(edges):
            if i == edge_idx:
                continue

            if uf.union(a, b):
                answer += weight
            
        parent = uf.find(0)

        return answer if all(uf.find(i) == parent for i in range(n)) else float('inf')
