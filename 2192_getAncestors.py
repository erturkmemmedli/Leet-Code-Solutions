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
