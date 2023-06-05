class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def union(self, a, b, cost):
        u = self.find(a)
        w = self.find(b)

        if u == w:
            return False

        self.parent[w] = u
        return True


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        def Kruskal():
            uf = UnionFind(n + 1)
            total_cost = 0

            for i, cost in enumerate(wells):
                pipes.append((0, i + 1, cost))

            pipes.sort(key = lambda x : x[2])

            for a, b, cost in pipes:
                if uf.union(a, b, cost):
                    total_cost += cost

            return total_cost

        def Prim():
            graph = defaultdict(list)

            for u, v, cost in pipes:
                graph[u].append([v, cost])
                graph[v].append([u, cost])

            for u, cost in enumerate(wells, 1):
                graph[u].append([0, cost])
                graph[0].append([u, cost])

            heap = [(0, 0)]
            visited = set()
            total_cost = 0

            while heap:
                cost, node = heappop(heap)

                if node not in visited:
                    visited.add(node)
                    total_cost += cost
                    
                    for neighbor, c in graph[node]:
                        if neighbor not in visited:
                            heappush(heap, [c, neighbor])

            return total_cost

        return Prim()
