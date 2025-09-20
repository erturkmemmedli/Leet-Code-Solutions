class Spreadsheet:

    def __init__(self, rows: int):
        self.matrix = [[0] * 26 for _ in range(rows)]

    def get_row_col(self, cell: str):
        col = ord(cell[0]) - ord('A') - 1
        row = int(cell[1:]) - 1
        return row, col
        
    def setCell(self, cell: str, value: int) -> None:
        row, col = self.get_row_col(cell)
        self.matrix[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self.get_row_col(cell)
        self.matrix[row][col] = 0

    def getValue(self, formula: str) -> int:
        cells = formula[1:].split("+")

        if cells[0][0].isalpha():
            r1, c1 = self.get_row_col(cells[0])
            v1 = self.matrix[r1][c1]
        else:
            v1 = int(cells[0])

        if cells[1][0].isalpha():
            r2, c2 = self.get_row_col(cells[1])
            v2 = self.matrix[r2][c2]
        else:
            v2 = int(cells[1])

        return v1 + v2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
