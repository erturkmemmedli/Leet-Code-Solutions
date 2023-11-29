class UnionFind:
    def find(self, parent, a):
        while a != parent[a]:
            a = parent[a]
        return a

    def union(self, parent, a, b):
        root_a = self.find(parent, a)
        root_b = self.find(parent, b)
        if root_a == root_b:
            return parent, False
        parent[root_b] = root_a
        return parent, True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()
        alice_edges = set()
        bob_edges = set()
        shared_edges = set()
        redundant_edges = 0

        for typ, a, b in edges:
            if typ == 1:
                alice_edges.add((a - 1, b - 1))
            elif typ == 2:
                bob_edges.add((a - 1, b - 1))
            else:
                if (a - 1, b - 1) in alice_edges:
                    alice_edges.remove((a - 1, b - 1))
                    redundant_edges += 1
                if (a - 1, b - 1) in bob_edges:
                    bob_edges.remove((a - 1, b - 1))
                    redundant_edges += 1
                shared_edges.add((a - 1, b - 1))

        shared_parent, redundant_edges = self.unification(uf, list(range(n)), shared_edges, redundant_edges)   
        alice_parent, redundant_edges = self.unification(uf, shared_parent[:], alice_edges, redundant_edges)
        bob_parent, redundant_edges = self.unification(uf, shared_parent[:], bob_edges, redundant_edges)

        return redundant_edges if self.connected(alice_parent) and self.connected(bob_parent) else -1

    def unification(self, uf, parent, edges, redundant):
        for a, b in edges:
            parent, condition = uf.union(parent, a, b)
            if not condition:
                redundant += 1
        return parent, redundant

    def connected(self, parent):
        roots = 0
        for i in range(len(parent)):
            if parent[i] == i:
                roots += 1
                if roots > 1:
                    return False
        return True

# Alternative solution

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        
        return a

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False
        
        if self.rank[ra] >= self.rank[rb]:
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
            
            self.parent[rb] = ra
        
        else:
            self.parent[ra] = rb

        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        common = []
        bob = []
        alice = []

        for typ, u, v in edges:
            match typ:
                case 1:
                    alice.append((u - 1, v - 1))
                case 2:
                    bob.append((u - 1, v - 1))
                case 3:
                    common.append((u - 1, v - 1))
   
        uf = UnionFind(n)
        removable = 0

        for u, v in common:
            if not uf.union(u, v):
                removable += 1

        uf_bob = UnionFind(n)
        uf_bob.parent = uf.parent.copy()
        uf_bob.rank = uf.rank.copy()

        for u, v in bob:
            if not uf_bob.union(u, v):
                removable += 1
            
        uf_alice = UnionFind(n)
        uf_alice.parent = uf.parent.copy()
        uf_alice.rank = uf.rank.copy()

        for u, v in alice:
            if not uf_alice.union(u, v):
                removable += 1

        parent_bob = uf_bob.find(0)
        parent_alice = uf_alice.find(0)

        for i in range(n):
            if uf_bob.find(i) != parent_bob or uf_alice.find(i) != parent_alice:
                return -1

        return removable
