class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def get_root(self):
        return self.root
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
        
    def find(self, root, word, replace):
        if not word:
            return root.end and replace == 0
        for child in root.children.keys():
            if child == word[0]:
                if self.find(root.children[child], word[1:], replace):
                    return True
            elif replace == 1:
                if self.find(root.children[child], word[1:], 0):
                    return True
        return False

class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)
                    
    def search(self, searchWord: str) -> bool:
        return self.trie.find(self.trie.get_root(), searchWord, 1)
        
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
