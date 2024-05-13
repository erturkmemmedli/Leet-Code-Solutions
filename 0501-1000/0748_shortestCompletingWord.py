class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = {}
        length = inf
        shortest = None

        for char in licensePlate:
            if char.isalpha():
                letters[char.lower()] = letters.get(char.lower(), 0) + 1
            
        for word in words:
            word_map = Counter(word)
            
            for key, val in letters.items():
                if key not in word_map:
                    break
                if word_map[key] < val:
                    break
            else:
                if len(word) < length:
                    length = len(word)
                    shortest = word

        return shortest
