class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # initialize fire's expansion time info
        fires = deque()
        fire_times = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fires.append((i, j))
                    fire_times[i][j] = 0

        # bfs for getting how fire is expanding in time
        while fires:
            r, c = fires.popleft()
            for row, col in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if m > row >= 0 <= col < n and grid[row][col] != 2 and fire_times[row][col] == float('inf'):
                    fires.append((row, col))
                    fire_times[row][col] = fire_times[r][c] + 1
        
        # initialize human position and distance map
        human = deque([(0, 0)])
        human_times = [[float('inf')] * n for _ in range(m)]
        human_times[0][0] = 0

        # bfs for finding shortest path to safehouse
        while human:
            r, c = human.popleft()
            if r == m - 1 and c == n - 1:
                break
            for row, col in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if m > row >= 0 <= col < n and grid[row][col] != 2 and human_times[row][col] == float('inf'):
                    human.append((row, col))
                    human_times[row][col] = human_times[r][c] + 1

        # generate map saving fire and human distance
        shortest_path_map = {}
        for i in range(m):
            for j in range(n):
                f = fire_times[i][j]
                h = human_times[i][j]
                shortest_path_map[h] = max(shortest_path_map.get(h, -float('inf')), f - h)

        # calculate max posible waiting time to start in case of fire expansion
        max_distance = human_times[-1][-1]
        final_pos_diff = fire_times[-1][-1] - human_times[-1][-1]
        final_pos_count = 0
        time_to_start = float('inf')
        for k, v in shortest_path_map.items():
            if 0 <= k <= max_distance:
                time_to_start = min(time_to_start, v)
                if v == final_pos_diff:
                    final_pos_count += 1

        # summarize findings
        if time_to_start != -float('inf') and final_pos_diff == time_to_start and final_pos_count == 1:
            return max(time_to_start, -1)
        return max(time_to_start - 1, -1) if time_to_start != float('inf') else 10**9
