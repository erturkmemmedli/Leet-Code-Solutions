class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        maximum = ""
        for word in dictionary:
            if len(maximum) >= len(word):
                continue
            i = 0
            j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(word):
                if len(maximum) != len(word):
                    maximum = max(maximum, word, key = len)
                else:
                    maximum = min(maximum, word)
        return maximum

# Alternative solution (which gives TLE error)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def getRoot(self):
        return self.root

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        self.maximum = ""
        root = trie.getRoot()
        path = ""
        self.dfs(s, root, path)
        return self.maximum

    def dfs(self, string, root, path):
        if not root:
            return
        for i, char in enumerate(string):
            if char in root.children:
                if root.children[char].end:
                    if len(self.maximum) != len(path + char):
                        self.maximum = max(self.maximum, path + char, key = len)
                    else:
                        self.maximum = min(self.maximum, path + char)
                self.dfs(string[i+1:], root.children[char], path + char)
