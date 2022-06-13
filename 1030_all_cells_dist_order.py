from collections import deque

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        Q = deque([[rCenter, cCenter]])
        myset = set()
        result = []
        while Q:
            r, c = Q.popleft()
            if (r, c) not in myset:
                myset.add((r, c))
                result.append([r, c])
                for i, j in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
                    if 0 <= i < rows and 0 <= j < cols:
                        Q.append((i, j))
        return result
      
# Alternative solution

class Solution1:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([(i, j) for i in range(rows) for j in range(cols)], key = lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
