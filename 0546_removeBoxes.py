class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            if i > j: return 0
            index = [x for x in range(i + 1, j + 1) if boxes[i] == boxes[x]  and (x == i + 1 or boxes[x] != boxes[x - 1])]
            answer = (k + 1) ** 2 + dp(i + 1, j, 0)
            return max([answer] + [dp(i + 1, x - 1, 0) + dp(x, j, k + 1) for x in index])
        return dp(0, len(boxes) - 1, 0)
