from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color = [None for _ in range(len(graph))]
        for i in range(len(graph)):
            if color[i] is None:
                color[i] = 'W'
                Q = deque([i])
                while len(Q) != 0:
                    vertex = Q.popleft()
                    for path in graph[vertex]:
                        if color[path] is None:
                            if color[vertex] == 'W':
                                Q.append(path)
                                color[path] = 'B'
                            if color[vertex] == 'B':
                                Q.append(path)
                                color[path] = 'W'
                        else:
                            if (color[vertex] == 'W' and color[path] == 'W') or (color[vertex] == 'B' and color[path] == 'B'):
                                return False
        return True