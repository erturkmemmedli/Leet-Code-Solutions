class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        order = []

        while heap:
            val, r, c = heappop(heap)
            order.append(val)

            for row, col in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if m > row >= 0 <= col < n and (row, col) not in visited:
                    visited.add((row, col))
                    heappush(heap, (grid[row][col], row, col))

        curr_max = -1

        for i in range(m * n):
            curr_max = max(curr_max, order[i])
            order[i] = curr_max

        answer = []

        for query in queries:
            idx = bisect_left(order, query)
            answer.append(idx)

        return answer
