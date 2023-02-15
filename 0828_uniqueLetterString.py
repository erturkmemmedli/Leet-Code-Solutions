class Solution:
    def uniqueLetterString(self, s: str) -> int:
        result = [0 for _ in range(len(s) + 1)]
        hashTable = [[-1, -1] for _ in range(26)]
        for i, char in enumerate(s):
            index = ord(char) - ord('A')
            first, second = hashTable[index]
            result[i + 1] = 1 + result[i] + (i - 1 - second) - (second - first)
            hashTable[index] = [second, i]
        return sum(result) % (10 ** 9 + 7)
