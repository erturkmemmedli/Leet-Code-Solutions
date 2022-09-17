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

# Alternative solution

class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        self.dfs(nums, output, [])
        return output
    
    def dfs(self, nums, output, path):
        if not nums:
            output.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], output, path + [nums[i]])
