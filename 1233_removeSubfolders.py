class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        node.isEnd = True

    def getRoot(self):
        return self.root

    def find(self, node, output, path):
        if node.isEnd:
            output.append(path)
            return
        for child in node.children:
            if node == self.root:
                self.find(node.children[child], output, path + child)
            else:
                self.find(node.children[child], output, path + '/' + child)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for path in folder:
            trie.insert(path.split('/'))
        root = trie.getRoot()
        output = []
        trie.find(root, output, "")
        return output
