class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [-1, 0, 1, 0, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    target = (i, j)
                if grid[i][j] == 'B':
                    box = (i, j)
                if grid[i][j] == 'S':
                    person = (i, j)

        def valid(row, col):
            return m > row >= 0 <= col < n and grid[row][col] != '#'

        def check(source, destination, box):
            queue = deque([source])
            visited = set()

            while queue:
                r, c = queue.popleft()
                if (r, c) == destination:
                    return True

                for i in range(4):
                    row, col = r + dirs[i], c + dirs[i + 1]
                    if valid(row, col) and (row, col) not in visited and (row, col) != box:
                        visited.add((row, col))
                        queue.append((row, col))

            return False

        queue = deque([(0, box, person)])
        visited = {box + person}

        while queue:
            distance, box, person = queue.popleft()
            if box == target:
                return distance

            for i in range(4):
                new_box = (box[0] + dirs[i], box[1] + dirs[i + 1])
                new_person = (box[0] - dirs[i], box[1] - dirs[i + 1])
                if valid(*new_box) and new_box + box not in visited:
                    if valid(*new_person) and check(person, new_person, box):
                        visited.add(new_box + box)
                        queue.append((distance + 1, new_box, box))

        return -1

# Alternative solution

from heapq import heappush, heappop

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [-1, 0, 1, 0, -1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    target_pos = (i, j)
                if grid[i][j] == 'B':
                    box_pos = (i, j)
                if grid[i][j] == 'S':
                    person_pos = (i, j)

        def heuristic(row, col):
            return abs(target_pos[0] - row) + abs(target_pos[1] - col)

        def is_valid_pos(row, col):
            return m > row >= 0 <= col < n and grid[row][col] != '#'

        heap = [[heuristic(*box_pos), 0, person_pos, box_pos]]
        visited = set()

        while heap:
            _, distance, person_pos, box_pos = heappop(heap)

            if box_pos == target_pos:
                return distance
            
            if (person_pos + box_pos) in visited:
                continue

            visited.add(person_pos + box_pos)

            for i in range(4):
                new_person_pos = (person_pos[0] + directions[i], person_pos[1] + directions[i + 1])

                if not is_valid_pos(*new_person_pos):
                    continue

                if new_person_pos == box_pos:
                    new_box_pos = (box_pos[0] + directions[i], box_pos[1] + directions[i + 1])

                    if not is_valid_pos(*new_box_pos):
                        continue

                    new_dist = distance + 1
                    heappush(heap, (heuristic(*new_box_pos) + new_dist, new_dist, new_person_pos, new_box_pos))
                else:
                    heappush(heap, (heuristic(*box_pos) + distance, distance, new_person_pos, box_pos))

        return -1
