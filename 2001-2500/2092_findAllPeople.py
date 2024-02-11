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
            if ra == 0 or rb == 0:
                self.parent[ra] = 0
                self.parent[rb] = 0
            else:
                self.parent[rb] = ra

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        uf.parent[firstPerson] = 0

        meetings.sort(key = lambda x: x[2])
        i = 0

        while i < len(meetings):
            meetings_at_same_time = [meetings[i]]

            while i < len(meetings) - 1 and meetings[i][2] == meetings[i + 1][2]:
                meetings_at_same_time.append(meetings[i + 1])
                i += 1
            
            for p1, p2, time in meetings_at_same_time:
                uf.union(p1, p2)

            for p1, p2, time in meetings_at_same_time:
                if uf.find(p1) != 0:
                    uf.parent[p1] = p1
                    uf.parent[p2] = p2

            i += 1

        return [i for i in range(n) if uf.find(i) == 0]
