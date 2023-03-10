class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        dp = [1, 1]
        temp = []
        for i in range(rowIndex-1):
            for j in range(1, i+2):
                temp.append(dp[j-1] + dp[j])
            dp = [1] + temp + [1]
            temp = []
        return dp

# Alternative solution

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]
        for i in range(rowIndex):
            dp = [1]
            for i in range(len(pascal) - 1):
                dp.append(pascal[i] + pascal[i + 1])
            dp.append(1)
            pascal = dp[:]
        return pascal
