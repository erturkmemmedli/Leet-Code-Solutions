class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for _ in range(numRows - 1):
            dp = [0] + pascal[-1] + [0]
            pascal.append([dp[i] + dp[i + 1] for i in range(len(dp) - 1)])
        return pascal
