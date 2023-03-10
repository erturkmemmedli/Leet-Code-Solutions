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

# Alternative solution

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(result, nums, [], 0)
        return result

    def backtrack(self, result, nums, currState, start):
        result.append(currState[:])
        for i in range(start, len(nums)):
            currState.append(nums[i])
            self.backtrack(result, nums, currState, i + 1)
            currState.pop()

# Alternative solution

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            for i in range(len(result)):
                subset = list(result[i])
                subset.append(num)
                result.append(subset)
        return result
