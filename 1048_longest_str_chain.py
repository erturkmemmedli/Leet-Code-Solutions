class Solution:
    def longestStrChain(self, words) -> int:
        words = sorted(words, key = lambda x: len(x))
        dictionary = {}
        for i in range(len(words)):
            if len(words[i]) == len(words[0]):
                dictionary[words[i]] = 1
            else:
                for j in range(len(words[i])):
                    temp = words[i][0:j] + words[i][j+1:]
                    if temp in dictionary:
                        if words[i] not in dictionary:
                            dictionary[words[i]] = dictionary[temp] + 1
                        else:
                            dictionary[words[i]] = max(dictionary[words[i]], dictionary[temp] + 1)
                if words[i] not in dictionary:
                    dictionary[words[i]] = 1
        return max(dictionary.values())
