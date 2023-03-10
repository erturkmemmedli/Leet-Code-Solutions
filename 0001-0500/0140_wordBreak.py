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
