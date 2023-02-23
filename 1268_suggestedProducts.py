from heapq import heappush, nsmallest

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = []
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def get_root(self):
        return self.root
    
    def insert(self, word, index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            heappush(node.children[char].index, index)
            node = node.children[char]
        
    def find(self, node, char):
        if char in node.children:
            result = nsmallest(3, node.children[char].index)
            return node.children[char], result
        else:
            return None, []   
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for i, word in enumerate(products):
            trie.insert(word, i)
        root = trie.get_root()
        output = []
        for i, char in enumerate(searchWord):
            root, result = trie.find(root, char)
            if result:
                temp = []
                for idx in result:
                    temp.append(products[idx])
                output.append(temp)
            else:
                output.append([])
                break
        output += [[]] * (len(searchWord) - i - 1)
        return output

# Alternative solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        
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

            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    def suggest(self, node, char):
        if node and char in node.children:
            return node.children[char], node.children[char].suggestions 
        return None, []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()

        for product in products:
            trie.insert(product)

        output = []
        root = trie.get_root()

        for char in searchWord:
            if not root:
                output.append([])
            else:
                root, suggestion = trie.suggest(root, char)
                output.append(suggestion)

        return output
