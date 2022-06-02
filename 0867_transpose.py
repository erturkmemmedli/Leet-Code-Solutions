class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(map(lambda x: x[i], matrix)) for i in range(len(matrix[0]))]

# Alternative solution

class Solution1:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transposed_matrix = [[0] * m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                transposed_matrix[row][col] = matrix[col][row]
        return transposed_matrix
