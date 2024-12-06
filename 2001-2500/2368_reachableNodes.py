from collections import defaultdict, deque

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        tree = defaultdict(list)
        restricted = set(restricted)
        visited = {0}
        queue = deque([0])
        count = 0

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        while queue:
            node = queue.popleft()
            count += 1

            for child in tree[node]:
                if child not in visited and child not in restricted:
                    visited.add(child)
                    queue.append(child)
                
        return count
