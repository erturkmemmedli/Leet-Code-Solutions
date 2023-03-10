class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        roads = set()
        self.reorder_count = 0
        for a, b in connections:
            roads.add((a,b))
            graph[a].append(b)
            graph[b].append(a)  
            
        def dfs(node, parent):
            if (parent, node) in roads:
                self.reorder_count += 1
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
                
        dfs(0, -1)
        return self.reorder_count
        
# Alternative solution

class Solution1:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        reorder_count = 0
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        queue = collections.deque([0])
        visited = set([0])
        while queue:
            node = queue.popleft()
            for child, cost in graph[node]:
                if child not in visited:
                    visited.add(child)
                    reorder_count += cost
                    queue.append(child)
        return reorder_count
