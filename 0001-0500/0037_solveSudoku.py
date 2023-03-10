from collections import defaultdict as D, deque as Q

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rowMap, self.columnMap, self.boxMap, self.mustBeFilled = D(set), D(set), D(set), Q()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.rowMap[i].add(board[i][j])
                    self.columnMap[j].add(board[i][j])
                    self.boxMap[3*(i//3) + j//3].add(board[i][j])
                else:
                    self.mustBeFilled.append((i, j))
        self.backtrack(board)
        
    def backtrack(self, board):
        if not self.mustBeFilled:
            return True
        i, j = self.mustBeFilled.popleft()
        for digit in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if digit not in self.rowMap[i] and digit not in self.columnMap[j] and digit not in self.boxMap[3*(i//3) + j//3]:
                self.rowMap[i].add(digit)
                self.columnMap[j].add(digit)
                self.boxMap[3*(i//3) + j//3].add(digit)
                board[i][j] = digit
                if self.backtrack(board):
                    return True
                else:
                    self.rowMap[i].remove(digit)
                    self.columnMap[j].remove(digit)
                    self.boxMap[3*(i//3) + j//3].remove(digit)
                    board[i][j] = "."
        self.mustBeFilled.appendleft((i, j))
        return False
