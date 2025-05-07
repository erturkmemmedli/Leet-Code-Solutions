class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        distance = [[inf] * n for _ in range(m)]
        distance[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            d, r, c = heappop(heap)

            if r == m-1 and c == n-1:
                return d

            for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                if m > row >= 0 <= col < n and distance[row][col] > max(distance[r][c], moveTime[row][col]) + 1:
                    distance[row][col] = max(distance[r][c], moveTime[row][col]) + 1
                    heappush(heap, (distance[row][col], row, col))
