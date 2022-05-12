class Solution:
    def permuteUnique(self, nums):
        length = len(nums)
        output = set()
        self.dfs(nums, output, [], length)
        return output
    
    def dfs(self, nums, output, path, length):
        if not nums:
            output.add(tuple(path))
        for i in range(len(nums)):
            self.dfs(nums[i+1:] + nums[:i], output, path + [nums[i]], length)
