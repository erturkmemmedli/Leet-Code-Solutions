class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        for j in range(n):
            max_val = -math.inf
            indexes = []

            for i in range(m):
                max_val = max(max_val, matrix[i][j])
                if matrix[i][j] == -1:
                    indexes.append(i)
                
            for idx in indexes:
                matrix[idx][j] = max_val
            
        return matrix
