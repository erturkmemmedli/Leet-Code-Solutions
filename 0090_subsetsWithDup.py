class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = set()
        path = []
        nums.sort()
        self.dfs(nums, output, path)
        return output
        
    def dfs(self, nums, output, path):
        output.add(tuple(path))
        for i in range(len(nums)):
            self.dfs(nums[i+1:], output, path + [nums[i]])
