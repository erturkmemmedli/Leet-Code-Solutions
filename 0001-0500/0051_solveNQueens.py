class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.output = []
        self.backtrack(n, set(), set(), set(), 0, [])
        chessBoard = []
        for board in self.output:
            newBoard = []
            for row, col in board:
                newBoard.append("." * col + 'Q' + "." * (n - col - 1))
            chessBoard.append(newBoard)
        return chessBoard
    
    def backtrack(self, n, columns, diagonals, antidiagonals, index, path):
        if index == n:
            self.output.append(path)
            return
        for i in range(n):
            if i not in columns and index - i not in diagonals and index + i not in antidiagonals:
                columns.add(i)
                diagonals.add(index - i)
                antidiagonals.add(index + i)
                self.backtrack(n, columns, diagonals, antidiagonals, index + 1, path + [(index, i)])
                columns.remove(i)
                diagonals.remove(index - i)
                antidiagonals.remove(index + i) 
