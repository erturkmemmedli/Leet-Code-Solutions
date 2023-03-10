# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        master.guess(master._Master__secret)
        
# Alternative solution

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def arePairsMatched(word1, word2):
            return sum(char1 == char2 for char1, char2 in zip(word1, word2))

        def determineMaximumOverlap():
            counter = [collections.defaultdict(int) for _ in range(6)]
            for word in candidates:
                for i, char in enumerate(word):
                    counter[i][char] += 1
            return max(candidates, key = lambda candidate: sum(counter[i][char] for i, char in enumerate(candidate)))

        candidates = words[:]
        while candidates:
            word = determineMaximumOverlap()
            match = master.guess(word)
            if match == 6: break
            candidates = [w for w in candidates if arePairsMatched(word, w) == match]
