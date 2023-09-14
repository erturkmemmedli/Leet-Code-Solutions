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
