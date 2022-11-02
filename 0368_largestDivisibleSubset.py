# Alternatice solution (which gives TLE error)

class Solution:
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
