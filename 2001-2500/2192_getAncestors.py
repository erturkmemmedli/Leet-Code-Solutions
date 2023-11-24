class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i:[] for i in range(n)}
        in_degree = {i:0 for i in range(n)}

        for start, end in edges:
            graph[start].append(end)
            in_degree[end] += 1

        queue = deque([node for node, degree in in_degree.items() if not degree])
        answer = [set() for _ in range(n)]

        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                answer[neighbor].add(node)
                
                for element in answer[node]:
                    answer[neighbor].add(element)

                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return [sorted(list(ans)) for ans in answer]

# Alternative solution

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i : [] for i in range(n)}
        outdegree = {i : 0 for i in range(n)}
        ancestors = [set() for i in range(n)]
        
        for src, des in edges:
            graph[des].append(src)
            outdegree[src] += 1
        
        start = [key for key, val in outdegree.items() if val == 0]
        visited = {key for key, val in graph.items() if len(val) == 0}

        def dfs(node):
            for ancestor in graph[node]:
                if ancestor not in visited:
                    visited.add(node)
                    dfs(ancestor)
                ancestors[node].add(ancestor)
                ancestors[node] |= ancestors[ancestor]

        for node in start:
            dfs(node)

        return [sorted(list(l)) for l in ancestors]
