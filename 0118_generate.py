class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for _ in range(numRows - 1):
            dp = [0] + pascal[-1] + [0]
            pascal.append([dp[i] + dp[i + 1] for i in range(len(dp) - 1)])
        return pascal

# Alternative solution

class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1, numRows):
            temp = [1]
            j = 1
            while j < len(dp[i-1]):
                temp.append(dp[i-1][j-1] + dp[i-1][j])
                j += 1
            temp.append(1)
            dp.append(temp)
        return dp

# Alternative solution

class Solution2:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        temp = []
        for i in range(1, numRows):
            temp = [1] + [triangle[i-1][j] + triangle[i-1][j-1] for j in range(1,i)] + [1]
            triangle.append(temp)
        return triangle
