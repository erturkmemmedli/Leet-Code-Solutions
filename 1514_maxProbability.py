class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i, [a, b] in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        probability = [0 if i != start else 1 for i in range(n)]
        queue = collections.deque([(start, 1)])
        while queue:
            node, prob = queue.popleft()
            if node == end:
                probability[end] == max(probability[end], prob)
                continue
            for kid, succ in graph[node]:
                if probability[kid] < prob * succ:
                    probability[kid] = prob * succ
                    queue.append((kid, prob * succ))
        return probability[end]
