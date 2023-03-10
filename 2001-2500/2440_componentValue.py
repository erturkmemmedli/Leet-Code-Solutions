class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        if not edges: return 0
        n = len(nums)
        m = max(nums)
        s = sum(nums)
        self.graph = collections.defaultdict(set)
        for a, b in edges:
            self.graph[a].add(b)
            self.graph[b].add(a)
        for i in range(m, s + 1):
            if s % i == 0:
                if not self.dfs(nums, 0, -1, i):
                    return s // i - 1

    def dfs(self, nums, curr, prev, target):
        val = nums[curr]
        for child in self.graph[curr] - {prev}:
            k = self.dfs(nums, child, curr, target)
            if k == -1: return -1
            val += k
        return val % target if val <= target else -1
