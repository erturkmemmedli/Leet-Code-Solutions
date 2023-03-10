class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        self.sumArray = [0]
        for num in nums:
            self.sumArray.append(self.sumArray[-1] + num)
        dp = [self.calculateAverage(i, n) for i in range(n)]
        #print(dp) # Monitor DP for k = 1, i.e. the average of entire array.
        for _ in range(k-1):
            for i in range(n):
                for j in range(i + 1, n):
                    #print(dp[i], self.calculateAverage(i, j), dp[j]) # Current case and average of rest are compared.
                    dp[i] = max(dp[i], self.calculateAverage(i, j) + dp[j])
                    #print(dp) # Very important line to monitor how DP changes in each iteration.
        return dp[0]

    def calculateAverage(self, a, b):
        return (self.sumArray[b] - self.sumArray[a]) / (b - a)
