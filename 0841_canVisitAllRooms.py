from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        Q = deque([0])
        while Q:
            room = Q.popleft()
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    Q.append(key)
        return len(visited) == len(rooms)
