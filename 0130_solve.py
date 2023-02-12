class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        queue = collections.deque()
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][n-1] == 'O':
                queue.append((i, n-1))
        for j in range(1, n-1):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[m-1][j] == 'O':
                queue.append((m-1, j))
        visited = set()
        while queue:
            row, col = queue.popleft()
            visited.add((row, col))
            for r, c in (row-1, col), (row+1, col), (row, col-1), (row, col+1):
                if m > r >= 0 <= c < n and (r, c) not in visited and board[r][c] == 'O':
                    visited.add((r, c))
                    queue.append((r ,c))
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    board[i][j] = 'X'

# Alternative solution

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        self.visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in self.visited:
                    self.region = []
                    self.isBorderRegion = False
                    self.traverseRegion(board, m, n, i, j)
                    if not self.isBorderRegion:
                        for row, col in self.region:
                            board[row][col] = 'X'                    

    def traverseRegion(self, board, m, n, row, col):
        if row < 0 or row >= m or col < 0 or col >= n:
            self.isBorderRegion = True
            return
        if (row, col) in self.visited or board[row][col] == 'X':
            return
        self.visited.add((row, col))
        self.region.append((row, col))
        self.traverseRegion(board, m, n, row - 1, col)
        self.traverseRegion(board, m, n, row + 1, col)
        self.traverseRegion(board, m, n, row, col - 1)
        self.traverseRegion(board, m, n, row, col + 1)
