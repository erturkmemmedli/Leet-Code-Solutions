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
