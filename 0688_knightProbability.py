from collections import deque, defaultdict

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0: return 1
        elif n < 3 or (n == 3 and row == 1 and column == 1): return 0
        probability = 1
        division_factor = 1
        queue = deque([defaultdict(int, {(row, column):1})])
        path_from_row_col = defaultdict(list)
        while queue:
            level = queue.popleft()
            new_level = defaultdict(int)
            total_temp = 0
            for r, c in level:
                if (r, c) not in path_from_row_col:
                    temp = 0
                    for i, j in (r-2,c-1),(r-2,c+1),(r-1,c-2),(r-1,c+2),(r+2,c-1),(r+2,c+1),(r+1,c-2),(r+1,c+2):
                        if 0 <= i < n > j >= 0:
                            path_from_row_col[(r, c)].append((i, j))
                            new_level[(i, j)] += level[(r, c)]
                            temp += 1
                    total_temp += (temp / 8) * level[(r, c)]
                else:
                    for x, y in path_from_row_col[(r, c)]:
                        new_level[(x, y)] += level[(r, c)]
                    total_temp += (len(path_from_row_col[(r, c)]) / 8) * level[(r, c)]
            if new_level:
                print(new_level)
                probability *= total_temp / division_factor
                queue.append(new_level)
                division_factor = sum(new_level.values())
            k -= 1
            if k == 0: break
        return probability

# Alternative solution (which gives MLE(memory limit exceeded) error)

class Solution1:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0: return 1
        elif n < 3 or (n == 3 and row == 1 and column == 1): return 0
        probability = 1
        division_factor = 1
        queue = collections.deque([[(row, column)]])
        while queue:
            level = queue.popleft()
            new_level = []
            total_temp = 0
            for r, c in level:
                temp = 0
                for i, j in (r-2,c-1),(r-2,c+1),(r-1,c-2),(r-1,c+2),(r+2,c-1),(r+2,c+1),(r+1,c-2),(r+1,c+2):
                    if 0 <= i < n > j >= 0:
                        new_level.append((i, j))
                        temp += 1
                total_temp += temp / 8
                temp = 0
            if new_level:
                probability *= total_temp / division_factor
                queue.append(new_level)
                division_factor = len(new_level)
            k -= 1
            if k == 0: break
        return probability
