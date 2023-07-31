class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rot = list(zip(*matrix[::-1]))
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rot[i][j]

# Alternative solution

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            self.swap(matrix, i, n-i)

    def swap(self, matrix, s, n):
        for i in range(s, n-1):
            matrix[s][i], matrix[i][n-1], matrix[n-1][n-1-i+s], matrix[n-1-i+s][s] = matrix[n-1-i+s][s], matrix[s][i], matrix[i][n-1], matrix[n-1][n-1-i+s]
