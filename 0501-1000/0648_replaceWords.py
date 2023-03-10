class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        hashset = set(dictionary)
        answer = ""
        flag = True
        temp = ""
        for i in range(len(sentence)):
            if sentence[i] != " ":
                if flag:
                    temp += sentence[i]
                    if temp in hashset:
                        answer = self.operation(answer, temp)
                        temp = ""
                        flag = False
            else:
                answer = self.operation(answer, temp)
                temp = ""
                flag = True
        if temp:
            answer = self.operation(answer, temp)
        return answer
    
    def operation(self, answer, temp):
        if not answer or answer[-1] == " ":
            answer += temp
        else:
            answer += " " + temp
        return answer
      
# Alternative solution

class Solution1:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        hashset = set(dictionary)
        words = sentence.split()
        answer = []
        for word in words:
            flag = True
            for i in range(1, len(word)):
                if word[:i] in hashset:
                    answer.append(word[:i])
                    flag = False
                    break
            if flag:
                answer.append(word)
        return " ".join(answer)
      
# Alternative solution

class TrieNode:
    def __init__(self):
        self.exist = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.exist = True
    
    def prefix(self, word):
        node = self.root
        prefix = ""
        for char in word:
            prefix += char
            if char not in node.children:
                return word
            else:
                if node.children[char].exist:
                    return prefix
                else:
                    node = node.children[char]
        return word
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        answer = []
        for word in sentence.split():
            answer.append(trie.prefix(word))
        return " ".join(answer)

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
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word
            node = node.children[char]
            if node.isEnd:
                return word[:i+1]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        candidate_words = sentence.split()
        output = []
        for word in candidate_words:
            output.append(trie.search(word))
        return " ".join(output)
