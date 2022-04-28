import heapq

class Solution:
    def minimumEffortPath(self, heights):
        row = len(heights)
        col = len(heights[0])
        adj = [[] for _ in range(row * col)]
        eff = [[] for _ in range(row * col)]
        for i in range(row):
            for j in range(col):
                if col * i + j > col - 1:
                    adj[col * i + j].append(col * i + j - col)
                    eff[col * i + j].append(abs(heights[i][j] - heights[i - 1][j]))
                if col * i + j > col * i:
                    adj[col * i + j].append(col * i + j - 1)
                    eff[col * i + j].append(abs(heights[i][j] - heights[i][j - 1]))
                if col * i + j < col * (i + 1) - 1:
                    adj[col * i + j].append(col * i + j + 1)
                    eff[col * i + j].append(abs(heights[i][j] - heights[i][j + 1]))
                if col * i + j < (row - 1) * col:
                    adj[col * i + j].append(col * i + j + col)
                    eff[col * i + j].append(abs(heights[i][j] - heights[i + 1][j]))        
        cost = [float('inf') if _ else 0 for _ in range(row * col)]
        H = [(cost[0], 0)]
        heapq.heapify(H)
        while H:
            item = heapq.heappop(H)
            vertex = item[1]
            weight = item[0]
            for i in adj[vertex]:
                temp = max(weight, eff[vertex][adj[vertex].index(i)])
                if temp < cost[i]:
                    cost[i] = temp
                    heapq.heappush(H, (cost[i], i))
        return cost[-1]