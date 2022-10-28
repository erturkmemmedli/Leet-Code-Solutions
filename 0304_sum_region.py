class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])
        self.H = {(0, 0) : self.matrix[0][0]}
        for row in range(1, self.m):
            self.H[(row, 0)] = self.H[(row-1, 0)] + self.matrix[row][0]
        for col in range(1, self.n):
            self.H[(0, col)] = self.H[(0, col-1)] + self.matrix[0][col]
        for row in range(1, self.m):
            for col in range(1, self.n):
                self.H[(row, col)] = self.H[(row, col-1)] + self.H[(row-1, col)] + self.matrix[row][col] - self.H[(row-1, col-1)]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.H[(row2, col2)]
        elif row1 == 0:
            return self.H[(row2, col2)] - self.H[(row2, col1-1)]
        elif col1 == 0:
            return self.H[(row2, col2)] - self.H[(row1-1, col2)]
        else:  
            return self.H[(row2, col2)] + self.H[(row1-1, col1-1)] - self.H[(row1-1, col2)] - self.H[(row2, col1-1)]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Alternative solution

class NumMatrix1:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])
        for row in range(1, self.m):
            self.matrix[row][0] = self.matrix[row-1][0] + self.matrix[row][0]
        for col in range(1, self.n):
            self.matrix[0][col] = self.matrix[0][col-1] + self.matrix[0][col]
        for row in range(1, self.m):
            for col in range(1, self.n):
                self.matrix[row][col] = self.matrix[row][col-1] + self.matrix[row-1][col] + self.matrix[row][col] - self.matrix[row-1][col-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        else:  
            return self.matrix[row2][col2] + self.matrix[row1-1][col1-1] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] 

# Alternative solution

class NumMatrix2:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.M = matrix
        for i in range(m):
            for j in range(1, n):
                self.M[i][j] += self.M[i][j-1]
        for i in range(1, m):
            for j in range(n):
                self.M[i][j] += self.M[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.M[row2][col2]
        if row1 > 0 and col1 > 0:
            result += self.M[row1-1][col1-1]
        if col1 > 0:
            result -= self.M[row2][col1-1]
        if row1 > 0:
            result -= self.M[row1-1][col2]
        return result
