class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c or (m == r and n == c):
            return mat
        result = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                result[i][j] = mat[(i * c + j) // n][(i * c + j) % n]
        return result
