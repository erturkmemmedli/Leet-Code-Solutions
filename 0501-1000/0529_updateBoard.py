from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board # if the clicked cell is mine, game over!
        m = len(board)
        n = len(board[0])
        count = 0
        for a, b in (r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1):
            if 0 <= a < m and 0 <= b < n and board[a][b] == 'M':
                count += 1
        if count > 0:
            board[r][c] = str(count)
            return board # if there is a mine around the clicked cell, the cell turns to the digit showing count of mine(s) around the cell.
        Q = deque([(r, c)])
        visited = set()
        while Q:
            r, c = Q.popleft()
            board[r][c] = 'B'
            if (r, c) not in visited:
                visited.add((r, c))
                for i, j in (r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1):
                    if 0 <= i < m and 0 <= j < n:
                        count = 0
                        for a, b in (i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1):
                            if 0 <= a < m and 0 <= b < n and board[a][b] == 'M':
                                count += 1
                        if count == 0:
                            Q.append((i,j))
                        else:
                            board[i][j] = str(count)
        return board # if the clicked cell is blank, all adjacent blank cells and cells with digits showing count of mine(s) around the cell are revealed.

# Alternative solution

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        self.direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        row, col = click
        self.dfs(board, m, n, row, col)
        return board

    def dfs(self, board, m, n, row, col):
        if m > row >= 0 <= col < n:
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return
            elif board[row][col] == 'E':
                numMines = 0
                for r, c in self.direction:
                    if m > row + r >= 0 <= col + c < n and board[row + r][col + c] == 'M':
                        numMines += 1
                if numMines:
                    board[row][col] = str(numMines)
                else:
                    board[row][col] = 'B'
                    for r, c in self.direction:
                        self.dfs(board, m, n, row + r, col + c)

# Alternative solution

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click

        if board[r][c] == "M":
            board[r][c] = "X"
            return board

        queue = deque([(r, c)])
        visited = {(r, c)}

        while queue:
            r, c = queue.popleft()
            mines = 0

            for row, col in [r-1,c-1], [r-1,c], [r-1,c+1], [r,c-1], [r,c+1], [r+1,c-1], [r+1,c], [r+1,c+1]:
                if m > row >= 0 <= col < n and board[row][col] == "M":
                    mines += 1

            if mines > 0:
                board[r][c] = str(mines)
                continue
            
            board[r][c] = "B"

            for row, col in [r-1,c-1], [r-1,c], [r-1,c+1], [r,c-1], [r,c+1], [r+1,c-1], [r+1,c], [r+1,c+1]:
                if m > row >= 0 <= col < n and board[row][col] == "E" and (row, col) not in visited:
                    visited.add((row, col))
                    queue.append((row, col))

        return board
