class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if k == 0:
            return [str(i) * n for i in range(1, 10)]
        graph = collections.defaultdict(list)
        for i in range(10):
            if i - k >= 0:
                graph[str(i)].append(str(i - k))
            if i + k < 10:
                graph[str(i)].append(str(i + k))
        queue = collections.deque(list(map(str, range(1, 10))))
        output = []
        while queue:
            node = queue.popleft()
            for number in graph[node[-1]]:
                candidate = node + number
                if len(candidate) == n:
                    output.append(int(candidate))
                else:
                    queue.append(candidate)
                candidate = ""
        return output
