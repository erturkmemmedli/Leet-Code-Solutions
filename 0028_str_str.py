class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

# Alternative solution

class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        hash_val = hash(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if hash_val == hash(haystack[i:i+len(needle)]):
                return i
        return -1

# Alternative solution

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        string = needle + '-' + haystack
        lps = self.KMP_prefix(string)
        for i in range(len(needle)+1, len(string)):
            if lps[i] == len(needle):
                return i - 2 * len(needle)
        return -1
        
    def KMP_prefix(self, pattern):
        prefix = [0] * len(pattern)
        border = 0
        for i in range(1, len(pattern)):
            while border > 0 and pattern[i] != pattern[border]:
                border = prefix[border - 1]
            if pattern[i] == pattern[border]:
                border += 1
            else:
                border = 0
            prefix[i] = border
        return prefix

# Alternative solution

class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        trie = Trie()
        for i in range(len(haystack)):
            trie.insert(haystack[i:], i)
        return trie.search(needle)
        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = -1
              
class Trie:
    def __init__(self):
        self.root = self.get_node()
    
    def get_node(self):
        return TrieNode()
    
    def indexing(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word, val):
        temp = self.root
        for i in range(len(word)):
            index = self.indexing(word[i])
            if not temp.children[index]:
                temp.children[index] = self.get_node()
            temp = temp.children[index]
            if temp.end == -1:
                temp.end = val
            
    def search(self, word):
        temp = self.root
        for i in range(len(word)):
            index = self.indexing(word[i])
            if not temp.children[index]:
                return -1
            temp = temp.children[index]
        return temp.end

# Alternative solution

class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        n = len(needle)
        string = needle + '$' + haystack
        return self.KMP(string, n)
         
    def KMP(self, string, n):
        l = len(string)
        prefix = [0] * l
        j = 0
        for i in range(1, l):
            while j > 0 and string[i] != string[j]:
                j = prefix[j - 1]
            if string[i] == string[j]:
                j += 1
            else:
                j = 0
            prefix[i] = j
            if prefix[i] == n:
                return i - 2 * n
        return -1
