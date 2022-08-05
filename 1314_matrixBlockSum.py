class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i-k >= 0:
                    if j-k >= 0:
                        answer[i][j] = sum([sum(x[j-k:j+k+1]) for x in mat[i-k:i+k+1]])
                    else:
                        answer[i][j] = sum([sum(x[0:j+k+1]) for x in mat[i-k:i+k+1]])
                else:
                    if j-k >= 0:
                        answer[i][j] = sum([sum(x[j-k:j+k+1]) for x in mat[0:i+k+1]])
                    else:
                        answer[i][j] = sum([sum(x[0:j+k+1]) for x in mat[0:i+k+1]])     
        return answer
      
# Alternative solution

class Solution1:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        prefix = [[0] * n for _ in range(m)]
        for i in range(m):
            prefix[i][0] = mat[i][0]
            for j in range(1, n):
                prefix[i][j] = mat[i][j] + prefix[i][j-1]
        for i in range(n):
            for j in range(1, m):
                prefix[j][i] = prefix[j][i] + prefix[j-1][i]
        for i in range(m):
            row_low, row_high = max(i-k, 0), min(i+k, m-1) 
            for j in range(n):
                col_low, col_high = max(j-k, 0), min(j+k, n-1)
                value = prefix[row_high][col_high]
                if row_low-1 >= 0:
                    value -= prefix[row_low-1][col_high]
                if col_low-1 >= 0:
                    value -= prefix[row_high][col_low-1]
                if row_low-1 >= 0 and col_low-1 >= 0:
                    value += prefix[row_low-1][col_low-1]
                mat[i][j] = value
        return mat
