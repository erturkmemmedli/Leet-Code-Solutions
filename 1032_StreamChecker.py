class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.letters = []
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        i = len(self.letters) - 1
        node = self.trie.root
        while i >= 0:
            if node.isEnd:
                return True
            if self.letters[i] not in node.children:
                return False
            node = node.children[self.letters[i]]
            i -= 1
        return node.isEnd

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
