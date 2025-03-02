from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        # You must choose nodes such that in each root-to-leaf combination, 
        # one node must be left unchosen, trying to achieve max sum of values.

        # Ex 1: answer could also be nodes [0, 2, 4] (leaving 1 for first root-to-leaf case, 
        # 5 for second root-to-leaf case, and 3 for third root-to-leaf case) or [0, 2, 5] 
        # since they also give 11 as answer.

        # But since the one who wrote this description is single-celled retard, 
        # it is impossible to understand anything from it if you don't catch it by chance.

        tree = defaultdict(list)
        total_sum = sum(values)
        visited = set()

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(node):
            if len(tree[node]) == 1 and node != 0:
                return values[node]
            
            total = 0
            visited.add(node)

            for neighbor in tree[node]:
                if neighbor in visited:
                    continue
                total += dfs(neighbor)
            
            return min(values[node], total)

        return total_sum - dfs(0)
