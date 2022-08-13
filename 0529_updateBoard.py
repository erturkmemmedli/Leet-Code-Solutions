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
