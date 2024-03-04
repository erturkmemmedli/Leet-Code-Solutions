class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = {i : [] for i in range(n)}
        indegree = {i : 0 for i in range(n)}
        time = [[t, t] for t in time]
        total_month = 0

        for prev_course, next_course in relations:
            graph[prev_course - 1].append(next_course - 1)
            indegree[next_course - 1] += 1
        
        queue = deque([i for i in range(n) if indegree[i] == 0])

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                time[neighbor][1] = max(time[neighbor][1], time[node][0] + time[neighbor][0])
                if indegree[neighbor] == 0:
                    time[neighbor][0] = time[neighbor][1]
                    queue.append(neighbor)

        return max(time[i][1] for i in range(n))
