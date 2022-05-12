class Solution:
    def permuteUnique(self, nums):
        output = set()
        self.dfs(nums, output, [])
        return output
    
    def dfs(self, nums, output, path):
        if not nums:
            output.add(tuple(path))
        for i in range(len(nums)):
            self.dfs(nums[i+1:] + nums[:i], output, path + [nums[i]])
