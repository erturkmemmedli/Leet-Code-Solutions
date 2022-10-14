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

    def search(self, queue, visited, word):
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                flag = True
                break
            if node.children[char].isEnd:
                part = word[i+1:]
                if part not in visited:
                    queue.append(word[i+1:])
            node = node.children[char]

class Solution:
    global flag
    flag = False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        visited = set()
        queue = collections.deque([s])
        while queue:
            string = queue.popleft()
            if flag:
                return False
            if string == "":
                return True
            if string not in visited:
                visited.add(string)
                trie.search(queue, visited, string)
        return False