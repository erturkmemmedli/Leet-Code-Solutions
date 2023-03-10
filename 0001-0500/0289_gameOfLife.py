class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        changed = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count_of_ones = 0
                for r, c in directions:
                    if 0 <= r+i < m and 0 <= c+j < n:
                        if ((r+i,c+j) not in changed and board[r+i][c+j] == 1) or ((r+i,c+j) in changed and board[r+i][c+j] == 0):
                            count_of_ones += 1
                if board[i][j] == 0:
                    if count_of_ones == 3:
                        board[i][j] = 1
                        changed.add((i,j))
                    else:
                        continue
                elif board[i][j] == 1:
                    if 2 <= count_of_ones <= 3:
                        continue
                    else:
                        board[i][j] = 0
                        changed.add((i,j))
