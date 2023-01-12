class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        self.set = set()
        self.concatenated = []
        for word in words:
            if self.dfs(word, []):
                self.concatenated.append(word)
        return self.concatenated

    def dfs(self, word, path):
        if not word and len(path) > 1:
            return True
        for i in range(1, len(word) + 1):
            if word[:i] in self.set:
                if self.dfs(word[i:], path + [word[:i]]):
                    return True
        if word and not path:
            self.set.add("".join(path) + word)
