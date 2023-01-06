class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        head = [sum(row[0] for row in mat)] + [0] * m
        heap = [head]
        step = 1
        visited = {tuple(head)}
        while heap:
            level = heapq.heappop(heap)
            total = level[0]
            if step == k:
                return level[0]
            else:
                step += 1
            for i, idx in enumerate(level):
                if i == 0:
                    continue
                if idx + 1 < n:
                    newLevel = []
                    newLevel.append(total + mat[i - 1][idx + 1] - mat[i - 1][idx])
                    for j in range(m):
                        if j == i - 1:
                            newLevel.append(idx + 1)
                        else:
                            newLevel.append(level[j + 1])
                    tlevel = tuple(newLevel)
                    if tlevel not in visited:
                        heapq.heappush(heap, newLevel)
                        visited.add(tlevel)
