class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            d1 = {}
            d2 = {}
            i = 0
            while i < len(word):
                if pattern[i] not in d1:
                    d1[pattern[i]] = word[i]
                elif d1[pattern[i]] != word[i]:
                    break
                if word[i] not in d2:
                    d2[word[i]] = pattern[i]
                elif d2[word[i]] != pattern[i]:
                    break
                i += 1
            if i == len(word):
                res.append(word)
        return res 
