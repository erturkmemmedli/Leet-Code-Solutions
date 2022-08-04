class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = set()
        path = []
        summ = 0
        visited = set()
        candidates = list(set(sorted(candidates)))
        self.dfs(sorted(candidates, reverse = True), target, output, path, summ)
        return output
    
    def dfs(self, candidates, target, output, path, summ):
        if summ == target:
            output.add(tuple(sorted(path)))
            return
        if summ > target:
            return
        for i in range(len(candidates)):
            div = target // candidates[i]
            for j in range(1, div+1):
                self.dfs(candidates[i+1:], target, output, path + [candidates[i]] * j, summ + candidates[i] * j)
