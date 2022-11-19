from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        visited = set()
        Q = deque([(sr, sc)])
        while Q:
            row, col = Q.popleft()
            if (row, col) not in visited:
                visited.add((row, col))
                for r, c in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                    if r >= 0 and c >= 0 and r < m and c < n:
                        if image[r][c] == oldColor:
                            Q.append((r, c))
                            image[r][c] = newColor
        return image

# Alternative solution

class Solution1:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        visited = set()
        self.dfs(image, sr, sc, m, n, oldColor, newColor, visited)
        return image
         
    def dfs(self, image, row, col, m, n, old, new, visited):
        if (row, col) not in visited:
            visited.add((row, col))
            for r, c in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                if r >= 0 and c >= 0 and r < m and c < n:
                    if image[r][c] == old:
                        image[r][c] = new
                        self.dfs(image, r, c, m, n, old, new, visited)
        return

# Alternative solution

from collections import deque

class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        start = image[sr][sc]
        Q = deque([[sr, sc]])
        visited = set()
        while Q:
            row, col = Q.popleft()
            if (row, col) not in visited:
                visited.add((row, col))
                image[row][col] = color
                for r, c in [row-1,col], [row+1,col], [row,col-1], [row,col+1]:
                    if 0 <= r < m and 0 <= c < n and image[r][c] == start:
                        Q.append([r, c])
        return image
