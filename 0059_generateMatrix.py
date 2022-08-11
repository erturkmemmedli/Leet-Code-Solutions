class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row_inc, col_inc, row_dec, col_dec = False, True, False, False
        matrix = [[0] * n for _ in range(n)]
        hashset = set()
        row = 0
        col = 0
        value = 1
        while value <= n ** 2:
            matrix[row][col] = value
            value += 1
            hashset.add((row,col))
            if row_inc:
                if 0 <= row < n - 1 and (row+1,col) not in hashset:
                    row += 1
                else:
                    col -= 1
                    row_inc, col_dec = False, True
            elif col_inc:
                if 0 <= col < n - 1 and (row,col+1) not in hashset:
                    col += 1
                else:
                    row += 1
                    col_inc, row_inc = False, True
            elif row_dec:
                if 0 < row <= n - 1 and (row-1,col) not in hashset:
                    row -= 1
                else:
                    col += 1
                    row_dec, col_inc = False, True
            elif col_dec:
                if 0 < col <= n - 1 and (row,col-1) not in hashset:
                    col -= 1
                else:
                    row -= 1
                    col_dec, row_dec = False, True
        return matrix
