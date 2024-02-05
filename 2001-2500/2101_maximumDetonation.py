class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        connections = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if self.areCirclesIntercected(bombs[i], bombs[j]):
                    connections[i].append(j)
        
        max_deto = 1

        for i in range(len(bombs)):
            queue = deque([i])
            visited = {i}
            deto = 0

            while queue:
                node = queue.popleft()
                deto += 1

                for child in connections[node]:
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
                    
            max_deto = max(max_deto, deto)
        
        return max_deto
        
    def areCirclesIntercected(self, circle1, circle2):
        dist = ((circle1[0] - circle2[0]) ** 2 + (circle1[1] - circle2[1]) ** 2) ** 0.5
        return circle1[2] >= dist
