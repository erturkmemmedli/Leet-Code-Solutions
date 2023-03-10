class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        answer = sum(i.count(1) for i in matrix)
        while m > 0 and n > 0:
            new_matrix = []
            for i in range(m-1):
                temp = []
                for j in range(n-1):
                    if matrix[i][j] == 1 and matrix[i+1][j] == 1 and matrix[i][j+1] == 1 and matrix[i+1][j+1] == 1:
                        temp.append(1)
                        answer += 1
                    else:
                        temp.append(0)
                new_matrix.append(temp)
            matrix = new_matrix
            m -= 1
            n -= 1
        return answer
      
# Alternative solution

class Solution1:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        answer = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if i and j:
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    else:
                        dp[i][j] = 1
                answer += dp[i][j]
        return answer

# Alternative solution

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] and matrix[i][j] <= matrix[i][j-1] and matrix[i][j] <= matrix[i-1][j] and matrix[i][j] <= matrix[i-1][j-1]:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
        
        return sum(matrix[i][j] for i in range(m) for j in range(n))
