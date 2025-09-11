class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        current = [None] * len(s)

        for i, char in enumerate(s):
            if char in ['a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E']:
                vowels.append(char)
            else:
                current[i] = char

        vowels.sort(key=lambda x: ord(x))
        j = 0

        for i in range(len(s)):
            if current[i] == None:
                current[i] = vowels[j]
                j += 1

        return "".join(current)
