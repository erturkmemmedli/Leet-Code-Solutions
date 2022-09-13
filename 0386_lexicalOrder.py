class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.list = []
        
    def insert(self, digit):
        temp = self.root
        for i in range(len(digit)):
            if int(digit[:i+1]) not in temp.children:
                temp.children[int(digit[:i+1])] = TrieNode()
            temp = temp.children[int(digit[:i+1])]
            
    def get_root(self):
        return self.root
        
    def dfs_sort(self, node):
        if not node.children:
            return
        for child in node.children:
            self.list.append(child)
            self.dfs_sort(node.children[child])
        return self.list

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie()
        for i in range(1, n+1):
            trie.insert(str(i))
        root = trie.get_root()
        return trie.dfs_sort(root)
