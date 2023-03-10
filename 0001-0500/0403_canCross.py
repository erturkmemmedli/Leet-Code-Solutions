class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.memo = set()
        target = stones[-1]
        stones = set(stones)
        return self.dfs(stones, target, 1, 1)

    def dfs(self, stones, target, current, speed):
        if (current, speed) in self.memo:
            return False
        if target == current:
            return True
        if target < current or current < 0 or speed <= 0 or current not in stones:
            return False
        for s in [speed - 1, speed, speed + 1]:
            if current + s in stones:
                if self.dfs(stones, target, current + s, s):
                    return True
        self.memo.add((current, speed))
