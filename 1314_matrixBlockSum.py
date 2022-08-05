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
