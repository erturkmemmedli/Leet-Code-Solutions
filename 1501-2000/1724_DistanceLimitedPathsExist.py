class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: List[List[int]]):
        self.graph = defaultdict(list)

        for a, b, distance in edgeList:
            self.graph[a].append((b, distance))
            self.graph[b].append((a, distance))

    def query(self, p: int, q: int, limit: int) -> bool:
        visited = set()
        queue = deque([p])

        while queue:
            node = queue.popleft()

            if node == q:
                return True

            if node not in visited:
                visited.add(node)

                for neighbor, cost in self.graph[node]:
                    if cost < limit:
                        queue.append(neighbor)

        return False

# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)
