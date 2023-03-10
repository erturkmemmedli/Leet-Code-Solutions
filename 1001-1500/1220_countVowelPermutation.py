class Solution:
    def __init__(self):
        self.vowelMap = {0: [0,1,0,0,0],
                         1: [1,0,1,0,0],
                         2: [1,1,0,1,1],
                         3: [0,0,1,0,1],
                         4: [1,0,0,0,0]}

    def countVowelPermutation(self, n: int) -> int:
        dp = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
        for _ in range(n-1):
            for i in range(5):
                temp = [0,0,0,0,0]
                for j in range(5):
                    if dp[i][j] > 0:
                        for k in range(5):
                            temp[k] += dp[i][j] * self.vowelMap[j][k]
                dp[i] = temp[:]
        return sum(sum(vowel) % 1_000_000_007 for vowel in dp) % 1_000_000_007
