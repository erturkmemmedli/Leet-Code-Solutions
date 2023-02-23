class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        self.flag = False
        return self.dfs(self.root, word)

    def dfs(self, node, word):
        if not word and not node.isEnd:
            return False
        if node.isEnd and not node.children and word:
            return False
        if not word and node.isEnd:
            self.flag = True
            return True
        if word[0] == '.':
            for child in node.children:
                self.dfs(node.children[child], word[1:])
                if self.flag:
                    return True
        else:
            if word[0] in node.children:
                return self.dfs(node.children[word[0]], word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# ALternative solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary1:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)

    def dfs(self, node, word, index):
        if index == len(word):
            return node.isEnd
        if word[index] == '.':
            for child in node.children:
                if self.dfs(node.children[child], word, index + 1):
                    return True
        if word[index] in node.children:
            return self.dfs(node.children[word[index]], word, index + 1)
        return False

# Alternative solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(node, word)

    def dfs(self, node, word):
        if not word:
            return node.isEnd
        if node.isEnd and not node.children:
            return False
        if word[0] == '.':
            for child in node.children:
                if self.dfs(node.children[child], word[1:]):
                    return True
        elif word[0] not in node.children:
            return False
        else:
            return self.dfs(node.children[word[0]], word[1:])
