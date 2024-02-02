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

    def search(self, word):
        node = self.root
        result = []

        for i, char in enumerate(word): 
            if node.isEnd:
                result.append(i)

            if char not in node.children:
                return result

            node = node.children[char]

        if node.isEnd:
            result.append(i + 1)

        return result

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        node = trie.root

        for word in wordDict:
            trie.insert(word)
        
        queue = deque([(s, [])])
        result = []

        while queue:
            string, words = queue.popleft()

            if not string:
                result.append(" ".join(words))

            candidates = trie.search(string)

            for index in candidates:
                queue.append((string[index:], words + [string[:index]]))

        return result

# Alternative solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        self.sentences = []
        self.search(trie.root, trie.root, s, [])
        return [" ".join(sentence) for sentence in self.sentences]

    def search(self, root, node, word, path):
        if not word:
            if path:
                self.sentences.append(path)
            return

        for i, char in enumerate(word):
            if char not in node.children:
                return
            
            node = node.children[char]

            if node.is_end:
                self.search(root, root, word[i+1:], path + [word[:i+1]])

# Alternative solution

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        output = []

        def dp(s, sentence):
            if not s:
                output.append(sentence)
                return

            for i in range(len(s)):
                head = s[:i+1]
                tail = s[i+1:]
                if head in wordDict:
                    dp(tail, sentence + " " + head if sentence else head)

        dp(s, "")
        return output
