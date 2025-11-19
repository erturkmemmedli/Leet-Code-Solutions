class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 0
        count = 1
        char = word[0]

        for i in range(1, len(word)):
            if word[i] == char:
                count += 1
            else:
                res += count - 1
                char = word[i]
                count = 1
            
        res += count
        return res
