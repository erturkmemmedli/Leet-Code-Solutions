class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowel = [1, 2, 3, 4, 5]
        for _ in range(1, n): vowel = [sum(vowel[:i+1]) for i in range(len(vowel))]
        return vowel[-1]
