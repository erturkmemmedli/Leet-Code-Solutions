class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i : [] for i in range(9)}
        columns = {j : [] for j in range(9)}
        grids = {k: [] for k in range(9)}
        for i in range(9):
            for j in range(9):
                k = (i // 3) * 3 + (j // 3)
                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].append(board[i][j])
                    if board[i][j] in columns[j]:
                        return False
                    else:
                        columns[j].append(board[i][j])
                    if board[i][j] in grids[k]:
                        return False
                    else:
                        grids[k].append(board[i][j])
        return True
