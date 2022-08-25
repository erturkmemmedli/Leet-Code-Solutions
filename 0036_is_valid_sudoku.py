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

# Alternative solution

class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hashset = set()
            for element in row:
                if element != "." and element not in hashset:
                    hashset.add(element)
                elif element in hashset:
                    return False        
        for col in zip(*board):
            hashset = set()
            for element in col:
                if element != "." and element not in hashset:
                    hashset.add(element)
                elif element in hashset:
                    return False
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                hashset = set()
                grid = [x[j:j+3] for x in board[i:i+3]]
                for a in range(len(grid)):
                    for b in range(len(grid)):
                        if grid[a][b] != "." and grid[a][b] not in hashset:
                            hashset.add(grid[a][b])
                        elif grid[a][b] in hashset:
                            return False
        return True
