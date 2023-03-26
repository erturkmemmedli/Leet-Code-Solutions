class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            if word not in visited:
                visited.add(word)
                for i in range(len(word)):
                    for j in string.ascii_lowercase:
                        candidate = word[:i] + j + word[i+1:]
                        if candidate in wordList and candidate not in visited:
                            queue.append((candidate, step + 1))
        return 0

# Alternative solution (which gives TLE error)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # construction of graph
        graph = collections.defaultdict(list)
        for word in wordList:
            if self.hasOneLetterDifference(beginWord, word):
                graph[beginWord].append(word)
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if self.hasOneLetterDifference(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        # breadth-first search
        queue = collections.deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            if word not in visited:
                visited.add(word)
                for kid in graph[word]:
                    if kid not in visited:
                        queue.append((kid, step + 1))
        return 0

    def hasOneLetterDifference(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
            if diff > 1:
                return False
        return diff == 1
        
# Alternative solution (which gives TLE error)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # construction of graph
        graph = collections.defaultdict(list)
        for word in wordList:
            if self.hasOneLetterDifference(beginWord, word):
                graph[beginWord].append(word)
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if self.hasOneLetterDifference(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        # breadth-first search
        heap = [(1, beginWord)]
        visited = set()
        while heap:
            step, word = heapq.heappop(heap)
            if word == endWord:
                return step
            for kid in graph[word]:
                if kid not in visited:
                    visited.add(kid)
                    heapq.heappush(heap, (step + 1, kid))
        return 0

    def hasOneLetterDifference(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
            if diff > 1:
                return False
        return diff == 1