class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for fr, to, pr in flights:
            graph[fr].append((to, pr))
        cost = [[inf] * (k + 2) for _ in range(n)]
        cost[src][0] = 0
        heap = [(0, src, 0)]
        while heap:
            _, node, stop = heapq.heappop(heap)
            for child, price in graph[node]:
                if stop + 1 <= k + 1 and cost[child][stop + 1] > price + cost[node][stop]:
                    cost[child][stop + 1] = price + cost[node][stop]
                    heapq.heappush(heap, (price + cost[node][stop], child, stop + 1))
        result = min(cost[dst])
        return result if result != inf else -1
