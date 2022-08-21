class Solution:
    def __init__(self):
        self.count = 0
    
    def countArrangement(self, n: int) -> int:
        path = []
        index = 1
        self.dfs(list(range(1, n+1)), path, index, n)
        return self.count
        
    def dfs(self, nums, path, index, n):
        if len(path) == n:
            self.count += 1
            return
        for i in range(len(nums)):
            if nums[i] % index == 0 or index % nums[i] == 0:
                self.dfs(nums[i+1:] + nums[:i], path + [nums[i]], index + 1, n)
