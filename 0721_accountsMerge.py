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
