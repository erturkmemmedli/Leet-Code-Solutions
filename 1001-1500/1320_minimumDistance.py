class Solution:
    def minimumDistance(self, word: str) -> int:
        dp = {(word[0], None): 0}
        for char in word[1:]:
            newDP = {}
            for (finger1, finger2), dist in dp.items():
                newDP[(char, finger2)] = min(newDP.get((char, finger2), inf), dist + self.manhattanDistance(finger1, char))
                newDP[(finger1, char)] = min(newDP.get((finger1, char), inf), dist + self.manhattanDistance(char, finger2))
            dp = newDP
        return min(dp.values())

    @lru_cache
    def manhattanDistance(self, a, b):
        if a is None or b is None:
            return 0
        x1, y1 = divmod(ord(a) - 65, 6)
        x2, y2 = divmod(ord(b) - 65, 6)
        return abs(x1 - x2) + abs(y1 - y2)
