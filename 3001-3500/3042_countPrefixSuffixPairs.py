class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if len(words[i]) <= len(words[j]):
                    l = len(words[i])
                    count += (words[j][:l] == words[j][-l:] == words[i])
                
        return count
