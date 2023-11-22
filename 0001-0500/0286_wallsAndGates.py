class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        gates = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i, j))
        for r, c in gates:
            for row, col in [r-1, c], [r, c-1], [r+1, c], [r, c+1]:
                if m > row >= 0 <= col < n  and rooms[row][col] != -1 and rooms[row][col] != 0:
                    self.bfs(rooms, m, n, row, col)
                
    def bfs(self, rooms, m, n, row, col):
        queue = deque([(row, col)])
        rooms[row][col] = 1 
        visited = {(row, col)}
        while queue:
            r, c = queue.popleft()
            for i, j in [r-1, c], [r, c-1], [r+1, c], [r, c+1]:
                if m > i >= 0 <= j < n and rooms[i][j] != -1 and rooms[i][j] != 0 and (i, j) not in visited:
                    rooms[i][j] = min(rooms[i][j], rooms[r][c] + 1)
                    queue.append((i, j))
                    visited.add((i, j))

# Alternative solution

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue = deque([(i, j)])
                    visited = set()
                    
                    while queue:
                        r, c = queue.popleft()
                        
                        for row, col in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                            if m > row >= 0 <= col < n and (row, col) not in visited and rooms[row][col] > rooms[r][c] + 1:
                                rooms[row][col] = rooms[r][c] + 1
                                visited.add((row, col))
                                queue.append((row, col))


# Alternative solution (which gives TLE error)

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        gates = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i, j))
        for r, c in gates:
            for row, col in [r-1, c], [r, c-1], [r+1, c], [r, c+1]:
                if m > row >= 0 <= col < n  and rooms[row][col] != -1 and rooms[row][col] != 0:
                    self.dfs(rooms, m, n,row , col, 0, set())
            
    def dfs(self, rooms, m, n, row, col, distance, visited):
        if m > row >= 0 <= col < n and rooms[row][col] != -1 and rooms[row][col] != 0 and (row, col) not in visited:
            visited.add((row, col))
            rooms[row][col] = min(rooms[row][col], distance + 1)
            self.dfs(rooms, m, n, row - 1, col, rooms[row][col], visited)
            self.dfs(rooms, m, n, row + 1, col, rooms[row][col], visited)
            self.dfs(rooms, m, n, row, col - 1, rooms[row][col], visited)
            self.dfs(rooms, m, n, row, col + 1, rooms[row][col], visited)
            visited.remove((row, col))

# Alternative solution

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                r, c = queue.popleft()

                for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                    if m > row >= 0 <= col < n and rooms[row][col] == 2**31-1:
                        rooms[row][col] = rooms[r][c] + 1
                        queue.append((row, col))

# Alternative solution

from collections import deque

class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
                
        while queue:
            r, c = queue.popleft()
            
            for row, col in (r-1, c), (r, c-1), (r+1, c), (r, c+1):
                if m > row >= 0 <= col < n and (row, col) not in visited and rooms[row][col] != -1:
                    rooms[row][col] = rooms[r][c] + 1
                    visited.add((row, col))
                    queue.append((row, col))
                
        return rooms
