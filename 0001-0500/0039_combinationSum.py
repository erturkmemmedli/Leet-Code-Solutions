class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = set()
        path = []
        summ = 0
        self.dfs(sorted(list(set(candidates)), reverse = True), target, output, path, summ)
        return output
    
    def dfs(self, candidates, target, output, path, summ):
        if summ == target:
            output.add(tuple(path))
            return
        if summ > target:
            return
        for i in range(len(candidates)):
            div = target // candidates[i]
            for j in range(1, div+1):
                self.dfs(candidates[i+1:], target, output, path + [candidates[i]] * j, summ + candidates[i] * j)

# Alternative solution

class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = set()
        self.dfs(sorted(list(set(candidates)), reverse = True), target, output, [])
        return output
    
    def dfs(self, candidates, target, output, path):
        if target == 0:
            output.add(tuple(path))
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            div = target // candidates[i]
            for j in range(1, div+1):
                self.dfs(candidates[i+1:], target - candidates[i] * j, output, path + [candidates[i]] * j)

# Alternative solution

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        self.dfs(candidates, target, output, [])
        return output
    
    def dfs(self, candidates, target, output, path):
        if target == 0:
            output.append(path)
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], output, path + [candidates[i]])

# Alternative solution

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = set()
        self.backtrack(candidates, target, [], 0)
        return list(self.result)

    def backtrack(self, nums, target, currState, currSum):
        if currSum > target:
            return
        elif currSum == target:
            self.result.add(tuple(sorted(currState[:])))
            return
        for i in range(len(nums)):
            currState.append(nums[i])
            currSum += nums[i]
            self.backtrack(nums, target, currState, currSum)
            currSum -= nums[i]
            currState.pop()

# Alternative solution

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result =[]
        self.backtrack(candidates, target, [], 0)
        return list(self.result)

    def backtrack(self, nums, target, currState, currSum):
        if currSum > target:
            return
        elif currSum == target:
            self.result.append(currState[:])
            return
        for i in range(len(nums)):
            currState.append(nums[i])
            currSum += nums[i]
            self.backtrack(nums[i:], target, currState, currSum)
            currSum -= nums[i]
            currState.pop()
