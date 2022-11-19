class Solution:
    def makeGraph(self, n, connections):
        graph = [[] for _ in range(n)]
        for con in connections:
            graph[con[0]].append(con[1])
            graph[con[1]].append(con[0])
        return graph
    
    def DFS(self, graph, visited, rank, lowest, previous_vertex, current_vertex, result):
        visited[current_vertex] = True
        lowest[current_vertex] = rank
        for next_vertex in graph[current_vertex]:
            if next_vertex == previous_vertex:
                continue
            if not visited[next_vertex]:
                self.DFS(graph, visited, rank + 1, lowest, current_vertex, next_vertex, result)
            lowest[current_vertex] = min(lowest[current_vertex], lowest[next_vertex])
            if lowest[next_vertex] >= rank + 1:
                result.append([current_vertex, next_vertex])            
    
    def criticalConnections(self, n, connections):
        graph = self.makeGraph(n, connections)
        visited = [False for _ in range(n)]
        rank = 0
        lowest = [i for i in range(n)]
        previous_vertex = -1
        current_vertex = 0
        result = []
        self.DFS(graph, visited, rank, lowest, previous_vertex, current_vertex, result)
        return result
