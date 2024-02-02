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

# Alternative solution

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) < len(dp) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                
                if dp[i]:
                    break
                
        return dp[0] == 1

# Alternative solution

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = {s}
        wordDict = set(wordDict)

        def dp(s):
            if not s:
                return True

            for i in range(len(s)):
                if s[:i+1] in wordDict and s[i+1:] not in seen:
                    seen.add(s[i+1:])
                    if dp(s[i+1:]):
                        return True
            
        return dp(s)
