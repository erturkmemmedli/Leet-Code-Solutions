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

# Alternative solution

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([endWord])
        visited = {endWord}
        path_length = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                word = queue.popleft()

                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        new_word = word[:i] + char + word[i+1:]

                        if new_word == beginWord:
                            return path_length + 1

                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)
                    
            path_length += 1

        return 0

# Alternative solution

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = set(wordList)

        if endWord not in graph: return 0

        level = {beginWord}
        length = 0

        while level:
            graph -= level
            length += 1

            if endWord in level: break

            new_level = set()

            for word in level:
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        new_word = word[:i] + char + word[i+1:]

                        if new_word in graph:
                            new_level.add(new_word)
                        
            level = new_level
        
        if endWord not in new_level: return 0
        
        return length
