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
