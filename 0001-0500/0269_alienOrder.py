class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.letters = set()
        
        for word in words:
            for letter in word:
                self.letters.add(letter)

        self.graph = defaultdict(set)
        self.indegree = {char : 0 for char in self.letters}
        
        for i in range(1, len(words)):
            if not self.compareWords(words[i-1], words[i]):
                return ""

        queue = deque([key for key, val in self.indegree.items() if val == 0])
        alien_dictionary = []
        
        while queue:
            node = queue.popleft()
            alien_dictionary.append(node)
            
            for neighbor in self.graph[node]:
                self.indegree[neighbor] -= 1
                
                if self.indegree[neighbor] == -1:
                    return ""
                    
                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return "".join(alien_dictionary) if len(alien_dictionary) == len(self.graph) else ""
        
    def compareWords(self, a, b):
        i = 0
        
        while i < min(len(a), len(b)):
            if a[i] != b[i]:
                if b[i] in self.graph[a[i]]:
                    return True

                self.graph[a[i]].add(b[i])
                self.indegree[b[i]] += 1
                return True
            
            i += 1

        return len(a) <= len(b)

# Alternative solution

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        indegree = {}
        
        for word in words:
            for char in word:
                graph[char] = []
                indegree[char] = 0

        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]

            for i in range(min(len(first), len(second))):
                if first[i] != second[i]:
                    graph[first[i]].append(second[i])
                    indegree[second[i]] += 1
                    break

                if i == min(len(first), len(second)) - 1 and len(first) > len(second):
                    return ""

        toposort = ""
        queue = deque([key for key, val in indegree.items() if val == 0])

        while queue:
            node = queue.popleft()
            toposort += node

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return toposort if len(toposort) == len(graph) else ""

# Alternative solution

from collections import deque

class Solution:
    def alienOrder(self, words):
        alphabet = set()
        
        for word in words:
            alphabet |= set(word)
            
        graph = {i : [] for i in alphabet}
        indegree = {i : 0 for i in alphabet}
        
        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
            flag = False
            
            for j in range(min(len(curr), len(prev))):
                if prev[j] != curr[j]:
                    graph[prev[j]].append(curr[j])
                    indegree[curr[j]] += 1
                    flag = True
                    break
            
            if not flag and len(prev) > len(next):
                return ""
                    
        queue = deque([key for key, val in indegree.items() if val == 0])
        order = ""
        
        while queue:
            node = queue.popleft()
            order += node
            
            for child in graph[node]:
                indegree[child] -= 1
                
                if indegree[child] == 0:
                    queue.append(child)
                    
        return order if len(order) == len(alphabet) else ""
