class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = set(wordList)
        if endWord not in graph:return []
        currLevel = {beginWord}
        self.parents = {}

        while currLevel:
            graph -= currLevel
            nextLevel = set()

            for word in currLevel:
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        newWord = word[:i] + char + word[i+1:]
                        if newWord in graph:
                            nextLevel.add(newWord)
                            if newWord not in self.parents:
                                self.parents[newWord] = []
                            self.parents[newWord].append(word)

            if endWord in nextLevel:
                break
            currLevel = nextLevel

        self.ladders = []
        self.dfs(beginWord, endWord, [])
        return self.ladders

    def dfs(self, begin, end, path):
        if begin == end:
            path.append(begin)
            self.ladders.append(path[::-1])
            return

        if end not in self.parents:
            return

        for word in self.parents[end]:
            self.dfs(begin, word, path + [end])

# Alternative solution (which gives TLE error)

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.graph = {}
        self.graph[beginWord] = []

        for word in wordList:
            if self.isNode(beginWord, word):
                self.graph[beginWord].append(word)
            
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.isNode(wordList[i], wordList[j]):
                    if wordList[i] not in self.graph:
                        self.graph[wordList[i]] = []
                    self.graph[wordList[i]].append(wordList[j])
                    if wordList[j] not in self.graph:
                        self.graph[wordList[j]] = []
                    self.graph[wordList[j]].append(wordList[i])

        self.parent = {}
        length = self.bfs(beginWord, endWord)
        if not length: return []

        self.ladders = []
        self.dfs(length, [], beginWord, endWord)
        return self.ladders

    def isNode(self, word1, word2):
        difference = 0

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                difference += 1
            if difference > 1:
                return False

        return difference == 1

    def bfs(self, beginWord, endWord):
        heap = [(1, beginWord)]
        visited = set()
        length = None

        while heap:
            distance, node = heappop(heap)
            visited.add(node)

            if length and length < distance:
                break

            if node == endWord:
                length = distance

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    heappush(heap, (distance + 1, neighbor))
                    if neighbor not in self.parent:
                        self.parent[neighbor] = set()
                    self.parent[neighbor].add(node)

        return length

    def dfs(self, length, path, beginWord, endWord):
        if beginWord == endWord:
            if len(path) == length - 1:
                path.append(endWord)
                self.ladders.append(path[::-1])
            return

        for node in self.parent[endWord]:
            self.dfs(length, path + [endWord], beginWord, node)

# Alternative solution (which gives TLE error)

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.ladder = []
        self.length = float("inf")
        self.backtrack(beginWord, endWord, wordList, [beginWord], set())
        return self.ladder

    def backtrack(self, start, end, array, path, visited):
        if start == end:
            if len(path) < self.length:
                self.length = len(path)
                self.ladder = [path[:]]
            elif len(path) == self.length:
                self.ladder.append(path[:])
            return

        if start not in visited:
            for word in array:
                if self.isNode(start, word):
                    visited.add(start)
                    self.backtrack(word, end, array, path + [word], visited)
                    visited.remove(start)

    def isNode(self, word1, word2):
        difference = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                difference += 1
            if difference > 1:
                return False
        return difference == 1

# Alternative solution (which gives TLE error)

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = {}
        graph[beginWord] = []

        for word in wordList:
            if self.isNode(beginWord, word):  
                graph[beginWord].append(word)
            
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if wordList[i] == beginWord or wordList[j] == beginWord:
                    continue
                if self.isNode(wordList[i], wordList[j]):
                    if wordList[i] not in graph:
                        graph[wordList[i]] = []
                    graph[wordList[i]].append(wordList[j])
                    if wordList[j] not in graph:
                        graph[wordList[j]] = []
                    graph[wordList[j]].append(wordList[i])

        self.ladder = []
        self.length = float("inf")
        self.backtrack(graph, beginWord, endWord, [beginWord], set())
        return self.ladder

    def backtrack(self, graph, start, end, path, visited):
        if start == end:
            if len(path) < self.length:
                self.length = len(path)
                self.ladder = [path[:]]
            elif len(path) == self.length:
                self.ladder.append(path[:])
            return
            
        if start not in visited:
            for neighbor in graph[start]:
                visited.add(start)
                self.backtrack(graph, neighbor, end, path + [neighbor], visited)
                visited.remove(start)
            
    def isNode(self, word1, word2):
        difference = 0

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                difference += 1
            if difference > 1:
                return False

        return difference == 1
