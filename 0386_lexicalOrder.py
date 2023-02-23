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

# Alternative solution

class Solution1:
    def lexicalOrder(self, n: int) -> List[int]:
        if n < 10:
            return list(range(1,n+1))
        result = []
        for i in range(1, 10):
            result.append(i)
            result += self.trie_dfs(i, n)
        return result
            
    def trie_dfs(self, start, n):
        result = []
        for i in range(10):
            new_start = start * 10 + i
            if new_start > n:
                break
            result.append(new_start)
            result += self.trie_dfs(new_start, n)
        return result

# Alternative solution

class TrieNode:
    def __init__(self):
        self.children = [[] for _ in range(10)]
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        return self.root

    def insert(self, number):
        node = self.root

        for num in number:
            if node.children[int(num)] == []:
                node.children[int(num)] = TrieNode()

            node = node.children[int(num)]

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie()

        for i in range(1, n + 1):
            trie.insert(str(i))

        root = trie.get_root()
        current = 0
        self.output = []

        self.dfs(root, current)

        return self.output
        
    def dfs(self, node, current):
        for i in range(10):
            if node.children[i]:
                self.output.append(current + i)
                self.dfs(node.children[i], 10 * (current + i))
            elif i != 0:
                return
