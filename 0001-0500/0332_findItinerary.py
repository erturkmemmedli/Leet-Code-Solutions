class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = collections.defaultdict(list)
        for fr, to in tickets:
            self.graph[fr].append(to)
        for node, neighbors in self.graph.items():
            self.graph[node] = sorted(neighbors, reverse = True)
        self.EulerPath = []
        self.dfs("JFK")
        return self.EulerPath[::-1]

    def dfs(self, node):
        while self.graph[node]:
            kid = self.graph[node].pop()
            self.dfs(kid)
        self.EulerPath.append(node)

# Alternative solution (which gives TLE error)

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for source, destination in tickets:
            graph[source].append(destination)

        for key in graph.keys():
            graph[key] = sorted(graph[key], reverse=True)

        
        def dfs(node, output):
            if len(output) == len(tickets) + 1:
                return True

            for i in range(len(graph[node])-1, -1, -1):
                candidate = graph[node].pop(i)
                output.append(candidate)
                if dfs(candidate, output):
                    return output
                output.pop()
                graph[node].insert(i, candidate)

        return dfs("JFK", ['JFK'])
