from itertools import combinations

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        self.n = n
        self.k = k
        self.memo = {}
        self.graph = {i : [] for i in range(n)}
        indegree = [0] * n

        for prev, next in relations:
            self.graph[prev - 1].append(next - 1)
            indegree[next - 1] += 1

        return self.backtrack((1 << n) - 1, tuple(indegree))
 
    def backtrack(self, mask, indegree):
        if not mask:
            return 0

        if (mask, indegree) in self.memo:
            return self.memo[(mask, indegree)]
        
        nodes = [i for i in range(self.n) if mask & 1 << i and indegree[i] == 0]
        ans = float('inf')

        for k_nodes in combinations(nodes, min(self.k, len(nodes))):
            new_mask, new_indegree = mask, list(indegree)
            
            for node in k_nodes:
                new_mask ^= 1 << node

                for child in self.graph[node]:
                    new_indegree[child] -= 1

            ans = min(ans, self.backtrack(new_mask, tuple(new_indegree)) + 1)
        
        self.memo[(mask, indegree)] = ans
        return ans
