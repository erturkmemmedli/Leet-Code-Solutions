from collections import deque

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.combinationList = deque()
        self.dfs(self.characters, self.combinationLength, self.combinationList, "")

    def next(self) -> str:
        return self.combinationList.popleft()

    def hasNext(self) -> bool:    
        return len(self.combinationList) > 0
        
    def dfs(self, chars, length, output, path):
        if len(path) == length:
            output.append(path)
            return
        for i in range(len(chars)):
            self.dfs(chars[i+1:], length, output, path + chars[i])

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
