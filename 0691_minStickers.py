class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        self.frequency = [collections.Counter(sticker) for sticker in stickers]
        answer = self.dp(target)
        return answer if answer < math.inf else -1

    @lru_cache
    def dp(self, target):
        if not target:
            return 0 
        answer = math.inf
        frequency = Counter(target)
        for counter in self.frequency: 
            if target[0] in counter: 
                newTarget = "".join(key * val for key, val in (frequency - counter).items())
                answer = min(answer, 1 + self.dp(newTarget))
        return answer
