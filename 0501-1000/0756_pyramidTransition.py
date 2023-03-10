class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.hashmap = defaultdict(set)
        for pattern in allowed:
            self.hashmap[pattern[:2]].add(pattern[-1])
        return self.dfs(bottom, "")
                
    def dfs(self, layer, path):
        if len(layer) == 1:
            return True        
        pattern = layer[:2]
        if pattern in self.hashmap:
            for item in self.hashmap[pattern]:
                if len(layer) <= 2:
                    if self.dfs(path + item, ""):
                        return True
                else:
                    if self.dfs(layer[1:], path + item):
                        return True
        return False

# Alternative solution (which gives TLE)

from collections import defaultdict, deque

class Solution1:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.hashmap = defaultdict(set)
        for pattern in allowed:
            self.hashmap[pattern[:2]].add(pattern[-1])
        self.queue = deque([bottom])
        self.already_existed = set([bottom])
        while self.queue:
            word = self.queue.popleft()
            temp = []
            for i in range(len(word)-1):
                part = word[i:i+2]
                if part in self.hashmap:
                    temp.append(part)
                else:
                    temp = []
                    break
            if not temp:
                continue
            self.dfs(temp, "", len(word)-1)
            if self.queue and len(self.queue[-1]) == 1:
                return True
        return False
                
    def dfs(self, pairs, path, length):
        if len(path) == length and path not in self.already_existed:
            self.already_existed.add(path)
            self.queue.append(path)
        if pairs and pairs[0] in self.hashmap:
            for i in range(len(pairs)):
                for j in self.hashmap[pairs[i]]:
                    for item in j:
                        self.dfs(pairs[i+1:], path + item, length)
