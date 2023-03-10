class Solution:
    def longestCommonPrefix(self, strs):
        output = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(output):
                if output[j] == strs[i][j]:
                    j += 1
                else:
                    break
            output = output[:j]
        return output

# Alternative solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i, char in enumerate(word):
            if node.isEnd:
                return word[:i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def prefix(self, word, answer):
        node = self.root
        for i, char in enumerate(word):
            if node.isEnd:
                return word[:i]
            if char not in node.children:
                node.isEnd = True
                return word[:i]
            node = node.children[char]
        node.isEnd = True
        return word 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        trie.insert(strs[0])
        answer = strs[0]
        for i in range(1, len(strs)):
            answer = trie.prefix(strs[i], answer)
        return answer
