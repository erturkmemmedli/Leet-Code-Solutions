from collections import defaultdict, deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indexMap = defaultdict(deque)
        for i, char in enumerate(s):
            indexMap[char].append(i)
        characters = []
        for i, char in enumerate(s):
            if char in characters:
                indexMap[char].popleft()
                continue
            while characters and char < characters[-1] and indexMap[characters[-1]]:
                characters.pop()
            characters.append(char)
            indexMap[char].popleft()
        return "".join(characters)
