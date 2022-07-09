class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        count = 0
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'X':
                    if row > 0 and board[row-1][col] == 'X':
                        continue
                    if col > 0 and board[row][col-1] == 'X':
                        continue
                    count += 1
        return count 
