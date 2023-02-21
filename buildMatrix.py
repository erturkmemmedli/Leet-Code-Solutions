class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Classic topological sort problem. Both for rows and columns, Kahn's Algorithm will be applied.
        # Topologically sorted row and columns will show the correct positions of numbers (1 to k) in matrix (k x k)

        rows = self.topologicalSort(k, rowConditions)
        cols = self.topologicalSort(k, colConditions)

        if rows == [] or cols == []:
            return []

        indices = {i: [] for i in range(1, k + 1)}

        for idx, row in enumerate(rows):
            indices[row].append(idx)

        for idx, col in enumerate(cols):
            indices[col].append(idx)

        matrix = [[0] * k for _ in range(k)]

        for num, [row, col] in indices.items():
            matrix[row][col] = num

        return matrix

    def topologicalSort(self, n, edges):
        graph = {i: [] for i in range(1, n + 1)}
        in_degree = {i: 0 for i in range(1, n + 1)}

        for start, end in edges:
            graph[start].append(end)
            in_degree[end] += 1

        queue = deque([node for node, degree in in_degree.items() if not degree])

        toposort = []

        while queue:
            node = queue.popleft()
            toposort.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return toposort if len(toposort) == n else []
