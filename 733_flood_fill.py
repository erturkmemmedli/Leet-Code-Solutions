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
