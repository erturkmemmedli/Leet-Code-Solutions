class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        impossibleToMove = set()
        bordersToCheck = []
        volumeOfWater = 0

        def determineSuitability(i, j):
            if (i, j) not in impossibleToMove:
                impossibleToMove.add((i, j))
                heapq.heappush(bordersToCheck, (heightMap[i][j], i, j))
                for r, c in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                    if m > r >= 0 <= c < n and (r, c) not in impossibleToMove and heightMap[r][c] >= heightMap[i][j]:
                        determineSuitability(r, c)

        for i in range(m):
            determineSuitability(i, 0)
            determineSuitability(i, n-1)

        for j in range(n):
            determineSuitability(0, j)
            determineSuitability(m-1, j)

        while bordersToCheck:
            height, i, j = heapq.heappop(bordersToCheck)
            for r, c in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if m > r >= 0 <= c < n and (r, c) not in impossibleToMove:
                    volumeOfWater += (height - heightMap[r][c])
                    heightMap[r][c] = height
                    determineSuitability(r, c)

        return volumeOfWater

# Alternative solution

class Solution1:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        currentLevel = 0
        volumeOfWater = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            currentLevel = max(currentLevel, height)
            for r, c in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if m > r >= 0 <= c < n and heightMap[r][c] != -1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    if heightMap[r][c] < currentLevel:
                        volumeOfWater += currentLevel - heightMap[r][c]
                    heightMap[r][c] = -1
        return volumeOfWater
