class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        countLetters = collections.defaultdict(int)
        for char in letters:
            countLetters[char] += 1
        self.output = 0
        self.combination(words, score, countLetters, [])
        return self.output

    def getScore(self, score, char):
        return score[ord(char) - 97]

    def combination(self, words, score, countLetters, path):
        print(words, countLetters, path)
        if not words:
            total = sum([self.getScore(score, char) for word in path for char in word])
            self.output = max(self.output, total)
            return
        for i, word in enumerate(words):
            wordCount = collections.defaultdict(int)
            for char in word:
                wordCount[char] += 1
            if all(key in countLetters and wordCount[key] <= countLetters[key] for key, val in wordCount.items()):
                for key, val in wordCount.items():
                    countLetters[key] -= wordCount[key]
                self.combination(words[i+1:], score, countLetters, path + [word])
                for key, val in wordCount.items():
                    countLetters[key] += wordCount[key]
            else:
                total = sum([self.getScore(score, char) for word in path for char in word])
                self.output = max(self.output, total)
