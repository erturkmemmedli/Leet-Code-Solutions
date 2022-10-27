class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        # construction of bitmask
        start = sum(col << (i * n + j) for i, row in enumerate(mat) for j, col in enumerate(mat[i]))
        # breadth-first search
        queue = collections.deque([[start, 0]])
        visited = {start}
        while queue:
            current, step = queue.popleft()
            if current == 0:
                return step
            for i in range(m):
                for j in range(n):
                    next = current
                    for r, c in (i,j), (i,j-1), (i,j+1), (i-1,j), (i+1,j):
                        if m > r >= 0 <= c < n:
                            next ^= 1 << (r * n + c)
                    if next not in visited:
                        queue.append([next, step + 1])
                        visited.add(next)
        return -1
