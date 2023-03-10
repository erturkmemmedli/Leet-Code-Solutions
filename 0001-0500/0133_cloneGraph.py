"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if not node.neighbors:
            return Node(1)
        self.hashmap = collections.defaultdict(set)
        self.visited = set()
        self.dfs(node, None)
        cloneNodes = [Node(i) for i in range(1, len(self.hashmap) + 1)]
        for i in range(len(cloneNodes)):
            cloneNodes[i].neighbors = [cloneNodes[key - 1] for key in self.hashmap[i + 1]]
        return cloneNodes[0]

    def dfs(self, node, parent):
        if node in self.visited:
            self.hashmap[parent.val].add(node.val)
            return
        else:
            self.visited.add(node)
            for neighbor in node.neighbors:
                self.hashmap[node.val].add(neighbor.val)
                self.dfs(neighbor, node)
