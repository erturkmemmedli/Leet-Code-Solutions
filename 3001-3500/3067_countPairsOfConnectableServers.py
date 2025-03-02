from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        graph = defaultdict(list)
        output = []

        for a, b, c in edges:
            graph[a].append((b, c))
            graph[b].append((a, c))

        def dfs(node, parent, total):
            result = int(total % signalSpeed == 0)

            for neighbor, cost in graph[node]:
                if neighbor == parent:
                    continue
                result += dfs(neighbor, node, total + cost)

            return result

        def solve(node):
            result = 0
            current = 0

            for neighbor, cost in graph[node]:
                dfs_result = dfs(neighbor, node, cost)
                result += dfs_result * current
                current += dfs_result
            
            return result

        for i in range(len(edges) + 1):
            output.append(solve(i))
        
        return output
