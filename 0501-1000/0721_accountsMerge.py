class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashmap = {}
        self.parent = [i for i in range(len(accounts))]
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                if email in hashmap:
                    self.union(hashmap[email], i)
                hashmap[email] = i
        hashmapModified = collections.defaultdict(list)
        for key, val in hashmap.items():
            hashmapModified[self.find(val)].append(key)
        return [[accounts[key][0]] + sorted(val) for key, val in hashmapModified.items()]

    def union(self, parent, child):
        self.parent[self.find(child)] = self.find(parent)
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

# Alternative solution

class Solution1:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                hashmap[email].append(i)
        self.graph = [[] for _ in range(len(accounts))]
        for val in hashmap.values():
            if len(val) > 1:
                for i in range(len(val)):
                    for j in range(len(val)):
                        if i != j:
                            self.graph[val[i]].append(val[j])
        self.connected_components = [i for i in range(len(accounts))]
        self.visited = set()
        for i in range(len(self.graph)):
            if i not in self.visited:
                self.cc = i
                self.dfs(i)
        inverseHashmap = collections.defaultdict(list)
        for key, val in hashmap.items():
            inverseHashmap[self.connected_components[val[0]]].append(key)
        return [[accounts[key][0]] + sorted(val) for key, val in inverseHashmap.items()]

    def dfs(self, node):
        if node not in self.visited:
            self.visited.add(node)
            self.connected_components[node] = self.cc
            for neighbor in self.graph[node]:
                self.dfs(neighbor)
