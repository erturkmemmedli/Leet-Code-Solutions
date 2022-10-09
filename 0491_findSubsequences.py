class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.subsequences = []
        self.dfs(nums, [])
        return set(self.subsequences)

    def dfs(self, nums, path):
        if len(path) >= 2:
            self.subsequences.append(tuple(path))
        for i in range(len(nums)):
            if not path:
                self.dfs(nums[i+1:], path + [nums[i]])
            else:
                if nums[i] >= path[-1]:
                    self.dfs(nums[i+1:], path + [nums[i]])
