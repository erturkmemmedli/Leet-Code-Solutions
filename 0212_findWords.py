class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.wordAwaiting = 0

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        self.wordAwaiting += 1
        node.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        node = trie.root
        result = []
        
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in node.children:
                    self.dfs(trie, node.children[char], board, i, j, m, n, char, result)

        return result
            
    def dfs(self, trie, node, board, r, c, m, n, path, result):
        if not node or trie.wordAwaiting == 0:
            return

        if node.isEnd:
            result.append(path)
            node.isEnd = False
            trie.wordAwaiting -= 1

        temp = board[r][c]
        board[r][c] = "#"

        for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
            if m > row >= 0 <= col < n:
                char = board[row][col]
                if char in node.children:
                    self.dfs(trie, node.children[char], board, row, col, m, n, path + char, result)

        board[r][c] = temp


# Alternative solution (which gives TLE error)

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

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        
        for word in words:
            trie.insert(word)

        result = []
        self.wordAwaiting = len(words)

        for i in range(m):
            for j in range(n):
                self.dfs(trie.root, board, i, j, m, n, "", result)

        return result
            
    def dfs(self, node, board, r, c, m, n, path, result):
        if self.wordAwaiting == 0:
            return

        if node.isEnd:
            result.append(path)
            node.isEnd = False
            self.wordAwaiting -= 1

        if r < 0 or r >= m or c < 0 or c >= n:
            return

        temp = board[r][c]

        if temp not in node.children:
            return

        board[r][c] = "#"

        for row, col in [r-1, c], [r+1, c], [r, c-1], [r, c+1]:
            self.dfs(node.children[temp], board, row, col, m, n, path + temp, result)

        board[r][c] = temp
