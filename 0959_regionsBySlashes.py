from collections import deque

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        matrix = [[1] * 3*n for _ in range(3*n)]
        for i, slash in enumerate(grid):
            for j, symbol in enumerate(slash):
                if symbol == ' ':
                    continue
                elif symbol == '/':
                    matrix[3*i+2][3*j] = matrix[3*i+1][3*j+1] = matrix[3*i][3*j+2] = 0
                elif slash[j] == '\\':
                    matrix[3*i][3*j] = matrix[3*i+1][3*j+1] = matrix[3*i+2][3*j+2] = 0
        Q = deque()
        visited = set()
        count = 0
        for i in range(3*n):
            for j in range(3*n):
                if matrix[i][j]:
                    if (i,j) not in visited:
                        visited.add((i,j))
                        Q.append((i,j))
                        while Q:
                            row,col = Q.popleft()
                            for r,c in [row-1,col], [row+1,col], [row,col-1], [row,col+1]:
                                if 0 <= r < 3*n and 0 <= c < 3*n and (r,c) not in visited and matrix[r][c]:
                                    visited.add((r,c))
                                    Q.append((r,c))
                        count += 1
        return count
