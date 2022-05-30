from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = set()
        Q = deque([])
        for row in range(m):
            for col in range(n):
                if not mat[row][col]:
                    visited.add((row, col))
                    Q.append((row, col))
        while Q:
            r, c = Q.popleft()
            for i, j in (r-1,c), (r+1,c), (r,c-1), (r,c+1):
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                    if mat[i][j]:
                        mat[i][j] = mat[r][c] + 1
                        visited.add((i, j))
                        Q.append((i, j))
        return mat
