class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [[1, i] for i in range(n)]
        maximum = 0
        maximumIndex = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    if dp[j][0] < dp[i][0] + 1:
                        dp[j][0] = dp[i][0] + 1 
                        dp[j][1] = i
                    if maximum < dp[j][0]:
                        maximum = dp[j][0]
                        maximumIndex = j
        result = collections.deque()
        while dp[maximumIndex][0] > 1:
            result.appendleft(nums[maximumIndex])
            maximumIndex = dp[maximumIndex][1]
        result.appendleft(nums[maximumIndex])
        return result

# Alternatice solution (which gives TLE error)

class Solution1:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        self.output = []
        self.dfs(nums, [])
        return self.output

    def dfs(self, nums, path):
        if not nums:
            if len(path) > len(self.output):
                self.output = path
            return
        for i in range(len(nums)):
            if not path:
                self.dfs(nums[i+1:], [nums[i]])
            elif nums[i] % path[-1] == 0:
                self.dfs(nums[i+1:], path + [nums[i]])
            if i == len(nums) - 1:
                if len(path) > len(self.output):
                    self.output = path
