# Alternative solution (which gives TLE error)

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        val_map = defaultdict(list)
        num_of_good_paths = len(vals)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i, val in enumerate(vals):
            val_map[val].append(i)
        
        val_map_sorted = sorted([(key, val) for key, val in val_map.items()])
        visited = set()

        def dfs(src, dest, seen):
            if src == dest:
                return True

            for child in graph[src]:
                if child in visited and child not in seen:
                    seen.add(child)
                    if dfs(child, dest, seen):
                        return True
                    seen.remove(child)

        for val, nodes in val_map_sorted:
            visited |= set(nodes)
            for i in range(len(nodes)):
                for j in range(i + 1, len(nodes)):
                    if dfs(nodes[i], nodes[j], {nodes[i]}):
                        num_of_good_paths += 1

        return num_of_good_paths

# Alternative solution (which gives TLE error)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node

    def union(self, node_a, node_b):
        root_a = self.find(node_a)
        root_b = self.find(node_b)
        if root_a != root_b:
            self.parent[root_b] = root_a

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        uf = UnionFind(len(vals))
        graph = defaultdict(list)
        val_map = defaultdict(set)
        num_of_good_paths = len(vals)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i, val in enumerate(vals):
            val_map[val].add(i)
        
        for val in sorted(val_map.keys()):
            for node in val_map[val]:
                for neighbor in graph[node]:
                    if vals[neighbor] <= val:
                        uf.union(node, neighbor)

            connected_components = defaultdict(int)
            for node in val_map[val]:
                connected_components[uf.find(node)] += 1

            for root, count in connected_components.items():
                num_of_good_paths += count * (count - 1) // 2

        return num_of_good_paths
