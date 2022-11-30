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
