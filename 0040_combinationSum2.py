from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target: return []
        output = set()
        dictionary = Counter(candidates)
        self.dfs(sorted(list(set(candidates))), target, dictionary, output, [])
        return output
        
    def dfs(self, candidates, target, dictionary, output, path):
        if target == 0:
            output.add(tuple(path))
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            for j in range(1, dictionary[candidates[i]] + 1):
                self.dfs(candidates[i+1:], target - candidates[i] * j, dictionary, output, path + [candidates[i]] * j)

# Alternative solution

from collections import Counter

class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        self.dfs(candidates, target, output, [])
        return output
        
    def dfs(self, candidates, target, output, path):
        if target == 0:
            output.append(path)
            return
        if target < 0:
            return
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates[i+1:], target - candidates[i], output, path + [candidates[i]])

# Alternative solution

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.result = []
        self.backtrack(candidates, target, [])
        return self.result

    def backtrack(self, nums, target, path):
        if target < 0:
            return
        elif target == 0:
            self.result.append(path[:])
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtrack(nums[i+1:], target - nums[i], path)
            path.pop()
