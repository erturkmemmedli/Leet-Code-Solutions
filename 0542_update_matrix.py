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

# Alternative solution

class Solution1:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            for col in range(n):
                if mat[row][col]:
                    mat[row][col] = float('inf')
                    if row and mat[row-1][col] < mat[row][col]:
                        mat[row][col] = mat[row-1][col] + 1
                    if col and mat[row][col-1] < mat[row][col]:
                        mat[row][col] = mat[row][col-1] + 1
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if mat[row][col]:
                    if row < m - 1 and mat[row][col] > mat[row+1][col]:
                        mat[row][col] = mat[row+1][col] + 1
                    if col < n - 1 and mat[row][col] > mat[row][col+1]:
                        mat[row][col] = mat[row][col+1] + 1
        return mat

# Alternative solution

class Solution1:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = set()
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        while queue:
            r, c = queue.popleft()
            for row, col in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if m > row >= 0 <= col < n and (row, col) not in visited:
                    mat[row][col] =  mat[r][c] + 1
                    queue.append((row, col))
                    visited.add((row, col))
        return mat
