class Solution:
    def totalNQueens(self, n: int) -> int:
        columns_where_queens_are_placed = [-1] * n  # here (i, array[i]) refers to (row, column) pair
        self.number_of_solutions = 0
        queen_index = 0
        self.backtracking(columns_where_queens_are_placed, queen_index)
        return self.number_of_solutions
    
    def backtracking(self, columns, index):
        if index == len(columns):
            self.number_of_solutions += 1
            return
        for i in range(len(columns)):
            columns[index] = i
            if self.is_queen_in_valid_position(columns, index):
                self.backtracking(columns, index + 1)
                
    def is_queen_in_valid_position(self, columns, index):
        for i in range(index):
            if columns[i] == columns[index] or abs(columns[index] - columns[i]) == index - i:
                return False
        return True
      
# Alternative solution

class Solution1:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        diagonals = set()
        antidiagonals = set()
        self.total = 0
        index = 0
        self.backtrack(n, columns, diagonals, antidiagonals, index)
        return self.total
    
    def backtrack(self, n, columns, diagonals, antidiagonals, index):
        if n == index:
            self.total += 1
            return
        for i in range(n):
            if i not in columns and index - i not in diagonals and index + i not in antidiagonals:
                columns.add(i)
                diagonals.add(index - i)
                antidiagonals.add(index + i)
                self.backtrack(n, columns, diagonals, antidiagonals, index + 1)
                columns.remove(i)
                diagonals.remove(index - i)
                antidiagonals.remove(index + i)
