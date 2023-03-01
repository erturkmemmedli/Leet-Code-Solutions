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

# Alternative solution

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.backtrack(nums, [], 0)
        return self.result

    def backtrack(self, nums, currState, start):
        if currState not in self.result:
            self.result.append(currState)
        for i in range(start, len(nums)):
            self.backtrack(nums, currState + [nums[i]], i + 1)

# Alternative solution

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.backtrack(nums, [], 0)
        return self.result

    def backtrack(self, nums, currState, start):
        self.result.append(currState)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums, currState + [nums[i]], i + 1)
