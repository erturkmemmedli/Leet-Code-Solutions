class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a
    
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.parent[ra] = rb


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        hamming_distance = n
        parent_map = defaultdict(list)

        for a, b in allowedSwaps:
            uf.union(min(a, b), max(a, b))

        for i in range(n):
            parent_map[uf.find(i)].append(i)
        
        for k, v in parent_map.items():
            temp_source = []
            temp_target = []
            for i in range(len(v)):
                temp_source.append(source[v[i]])
                temp_target.append(target[v[i]])
            common = Counter(temp_source) & Counter(temp_target)
            hamming_distance -= sum(common.values())

        return hamming_distance
