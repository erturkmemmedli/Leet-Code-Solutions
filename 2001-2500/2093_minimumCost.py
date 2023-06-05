class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = {i : [] for i in range(n)}

        for a, b, cost in highways:
            graph[a].append((b, cost))
            graph[b].append((a, cost))

        costs = {(discount, node) : float('inf') for discount in range(discounts + 1) for node in range(n)}
        heap = [(0, discounts, 0)]

        while heap:
            curr_cost, discount, node = heappop(heap)

            if node == n - 1:
                return curr_cost

            for neighbor, cost in graph[node]:
                if curr_cost + cost < costs[(discount, neighbor)]:
                    costs[(discount, neighbor)] = curr_cost + cost
                    heappush(heap, (curr_cost + cost, discount, neighbor))
                    
                if discount and curr_cost + cost // 2 < costs[(discount - 1, neighbor)]:
                    costs[(discount - 1, neighbor)] = curr_cost + cost // 2
                    heappush(heap, (curr_cost + cost // 2, discount - 1, neighbor))

        return -1

# Alternative solution (which gives TLE error)

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        self.graph = {i : [] for i in range(n)}

        for a, b, cost in highways:
            self.graph[a].append((b, cost))
            self.graph[b].append((a, cost))

        self.minimum_cost = float('inf')
        self.dfs(0, n - 1, {0}, discounts, 0)
        return self.minimum_cost if self.minimum_cost != float('inf') else -1

    def dfs(self, source, destination, visited, discounts, total_cost):
        if discounts < 0:
            return

        if source == destination:
            self.minimum_cost = min(self.minimum_cost, total_cost)
            return

        for neighbor, cost in self.graph[source]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, destination, visited, discounts - 1, total_cost + cost // 2)
                self.dfs(neighbor, destination, visited, discounts, total_cost + cost)
                visited.remove(neighbor)
