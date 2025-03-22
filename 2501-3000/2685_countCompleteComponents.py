class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
                

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edge_map = defaultdict(int)
        parent_map = {}
        count = 0

        for a, b in edges:
            uf.union(a, b)
            edge_map[a] += 1

        for i in range(n):
            parent = uf.find(i)
            if parent not in parent_map:
                parent_map[parent] = [0, 0]
            parent_map[parent][0] += 1
            parent_map[parent][1] += edge_map[i]
        
        for k, v in parent_map.items():
            if v[0] * (v[0] - 1) // 2 == v[1]:
                count += 1

        return count
