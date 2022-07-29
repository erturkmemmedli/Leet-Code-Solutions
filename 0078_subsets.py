class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []
        self.dfs(nums, output, path)
        return output
        
    def dfs(self, nums, output, path):
        output.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], output, path + [nums[i]])
        return
