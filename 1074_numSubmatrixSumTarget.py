class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n-1):
                matrix[i][j+1] += matrix[i][j]
        result = 0
        for i in range(n):
            for j in range(i, n):
                presum = collections.defaultdict(int, {0: 1})
                temp = 0
                for k in range(m):
                    temp += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    result += presum[temp - target]
                    presum[temp] += 1
        return result
