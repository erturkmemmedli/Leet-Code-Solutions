from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for start, end in paths:
            graph[start].append(end)
            graph[end].append(start)
        flowers = [0] * n
        for i in range(n):
            temp = []
            for garden in graph[i+1]:
                temp.append(flowers[garden-1])
            for j in range(1, 5):
                if j not in temp:
                    flowers[i] = j
                    break
        return flowers
