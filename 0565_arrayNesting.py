class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        self.result = 0
        visited = set()
        for i in range(len(nums)):
            if i not in visited:
                self.dfs(nums, i, 0, visited)
        return self.result
        
    def dfs(self, nums, i, count, visited):
        if i not in visited:
            count += 1
            visited.add(i)
            return self.dfs(nums, nums[i], count, visited)
        else:
            self.result = max(self.result, count)
            return 
