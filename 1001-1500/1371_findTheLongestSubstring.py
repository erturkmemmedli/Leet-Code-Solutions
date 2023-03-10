class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        visited = {0: -1}
        result = 0
        current = 0
        for i, char in enumerate(s):
            current ^= 1 << ("aeiou".find(char) + 1) >> 1
            visited.setdefault(current, i)
            result = max(result, i - visited[current])
        return result
