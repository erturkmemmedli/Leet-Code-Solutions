class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * 3
        for i in range(len(stoneValue)-1, -1, -1):
            dp[i%3] = max(sum(stoneValue[i:i+k]) - dp[(i+k)%3] for k in range(1, 4))
        return "Tie" if dp[0] == 0 else "Alice" if dp[0] > 0 else "Bob"
