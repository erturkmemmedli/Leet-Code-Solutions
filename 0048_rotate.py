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
