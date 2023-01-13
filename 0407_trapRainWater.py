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
