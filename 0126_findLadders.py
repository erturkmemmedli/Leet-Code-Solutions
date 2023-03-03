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
