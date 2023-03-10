class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        output = []
        start = 0
        end = len(graph) - 1        
        self.dfs(graph, path, output, start, end)
        return output

    def dfs(self, graph, path, output, start, end):
        if start == end:
            output.append(path)
        for neighbor in graph[start]:
            self.dfs(graph, path + [neighbor], output, neighbor, end)
