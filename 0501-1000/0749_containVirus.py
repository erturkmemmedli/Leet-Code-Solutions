from collections import deque
from heapq import heappush, heappop

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        number_of_walls = 0
        
        def breadth_first_search():
            virus_zone = []
            visited = set()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        # finding every disconnected virus areas
                        queue = deque([(i, j)])
                        virus_area = {(i, j)}
                        while queue:
                            r, c = queue.popleft()
                            for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
                                if m > row >= 0 <= col < n and isInfected[row][col] == 1 and (row, col) not in virus_area:
                                    queue.append((row, col))
                                    visited.add((row, col))
                                    virus_area.add((row, col))
                        # prioritizing most dangerous virus area
                        potential_area = set()
                        wall = 0
                        for r, c in virus_area:
                            for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
                                if m > row >= 0 <= col < n and isInfected[row][col] == 0:
                                    potential_area.add((row, col))
                                    wall += 1
                        heappush(virus_zone, (-len(potential_area), wall, virus_area, potential_area))
            return virus_zone
        
        # applying breadth-first search algorithm to examine virus propogation
        virus_zone = breadth_first_search()
        # preventive quarantine measures
        while virus_zone:
            _, wall, virus_area, potential_area = heappop(virus_zone)
            number_of_walls += wall
            # applying quarantine measure on most dangerous infected area
            for row, col in virus_area:
                isInfected[row][col] = 2
            # virus is spreading in other infected areas
            for _, _, _, potential_area in virus_zone:
                for row, col in potential_area:
                    isInfected[row][col] = 1
            # applying breadth-first search algorithm to examine virus propogation
            virus_zone = breadth_first_search()
        return number_of_walls
