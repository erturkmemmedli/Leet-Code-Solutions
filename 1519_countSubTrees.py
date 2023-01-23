class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.result = [0] * n
        self.graph = collections.defaultdict(list)
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.visited = set()
        self.dfs(labels, 0, labels[0])
        return self.result

    def dfs(self, labels, node, label):
        if node not in self.visited:
            self.visited.add(node)
            hashmap = collections.Counter({label: 1})
            for kid in self.graph[node]:
                if kid not in self.visited:
                    hashmap += self.dfs(labels, kid, labels[kid])
            self.result[node] = hashmap[label]
            return hashmap
