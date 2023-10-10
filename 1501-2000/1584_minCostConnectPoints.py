class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.rank = 0
        
class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

class Solution:
    def MakeSet(self, i, x, y, nodes):
        nodes.append(Node(x, y, i))
        
    def Find(self, i, nodes):
        if i != nodes[i].parent:
            nodes[i].parent = self.Find(nodes[i].parent, nodes)
        return nodes[i].parent
    
    def Union(self, i, j, nodes):
        i_id = self.Find(i, nodes)
        j_id = self.Find(j, nodes)
        if i_id == j_id:
            return False
        if nodes[i_id].rank > nodes[j_id].rank:
            nodes[j_id].parent = i_id
        else:
            nodes[i_id].parent = j_id
            if nodes[i_id].rank == nodes[j_id].rank:
                nodes[j_id].rank += 1
        return True
        
    def minCostConnectPoints(self, points):
        self.result = 0
        self.nodes = []
        for i in range(0, len(points)):
            self.MakeSet(i, points[i][0], points[i][1], self.nodes)
        self.edges = []
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                self.cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                self.edges.append(Edge(i, j, self.cost))
        self.edges = sorted(self.edges, key = lambda e: e.cost)
        for edge in self.edges:
            
            if self.Find(edge.u, self.nodes) != self.Find(edge.v, self.nodes):
                self.result += edge.cost
                self.Union(edge.u, edge.v, self.nodes)
        return self.result 
 
# Alternative solution

class Solution1:
    def minCostConnectPoints(self, points):
        dictionary = {}
        cost = 0
        for i, (x, y) in enumerate(points):
            if i == 0:
                dictionary[(x,y)] = 0
            else:
                dictionary[(x,y)] = float('inf')
        while len(dictionary) != 0:
            x, y = min(dictionary, key = dictionary.get)
            cost += dictionary.pop((x, y))
            for xi, yi in dictionary:
                dictionary[(xi, yi)] = min(dictionary[(xi, yi)], abs(x - xi) + abs(y - yi))
        return cost

# Alternative solution

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node

    def union(self, node_a, node_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)

        if parent_a != parent_b:
            self.parent[parent_b] = parent_a
            return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind(len(points))
        cost_heap = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = self.manhattanDistance(points[i], points[j])
                heappush(cost_heap, (distance, i, j))
            
        min_cost = 0

        while cost_heap:
            distance, x, y = heappop(cost_heap)

            if uf.union(x, y):
                min_cost += distance

        return min_cost

    def manhattanDistance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return abs(x1 - x2 )+ abs(y1 - y2)
