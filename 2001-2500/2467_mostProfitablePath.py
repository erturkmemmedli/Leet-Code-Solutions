class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        parents = [None] * len(amount)
        visited = {bob}
        queue = deque([(bob, 1)])

        while queue:
            node, dist = queue.popleft()

            if node == 0:
                break

            for child in graph[node]:
                if child not in visited:
                    parents[child] = node
                    visited.add(child)
                    queue.append((child, dist + 1))
        
        bob_path = [0]
        i = 0

        while parents[i] != None:
            bob_path.append(parents[i])
            i = parents[i]

        m = len(bob_path)
        n = m // 2

        if m % 2 == 1:
            amount[bob_path[n]] //= 2
            for i in range(n + 1, m):
                amount[bob_path[i]] = 0
        else:
            for i in range(n, m):
                amount[bob_path[i]] = 0

        def dfs(node, profit, visited):
            if node != 0 and len(graph[node]) == 1:
                self.max_profit = max(self.max_profit, profit + amount[node])

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, profit + amount[node], visited)
                    visited.remove(child)
            
        self.max_profit = -float('inf')
        dfs(0, 0, {0})
        return self.max_profit
