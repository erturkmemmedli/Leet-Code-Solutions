class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = len)
        s = set("")
        out = "~"
        for word in words:
            if len(word) == 1:
                s.add(word)
                out = min(out, word)
            else:
                if word[:-1] in s:
                    s.add(word)
        for word in words:
            if word[:-1] in s:
                if len(word) == len(out):
                    out = min(out, word)
                else:
                    out = word
        return out if out != '~' else ""

# Alternative solution

class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        flag = True
        for i, char in enumerate(word):
            if char not in node.children:
                if i < len(word) - 1:
                    flag = False
                    break
                else:
                    node.children[char] = TrieNode()
            node = node.children[char]
        return flag

class Solution1:
    def longestWord(self, words: List[str]) -> str:
        longest = ""
        words.sort(key = len)
        trie = Trie()
        for word in words:
            if trie.insert(word):
                if len(word) == len(longest):
                    longest = min(longest, word)
                else:
                    longest = max(longest, word, key = len)
        return longest
