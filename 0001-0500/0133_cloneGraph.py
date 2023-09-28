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

# Alternative solution

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        
        hashmap = {}
        visited = set()
        queue = deque([node])

        while queue:
            curr_node = queue.popleft()
            
            if curr_node in visited:
                continue

            visited.add(curr_node)

            if curr_node.val not in hashmap:
                hashmap[curr_node.val] = []
            
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                hashmap[curr_node.val].append(neighbor.val)

        nodes = [Node(i + 1) for i in range(len(hashmap))]

        for key, val in hashmap.items():
            nodes[key - 1].neighbors = [nodes[n - 1] for n in val]

        return nodes[node.val - 1]

# Alternative solution

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        self.graph_dict = {}
        self.dfs(node)
        
        node_map = {i : Node(i) for i in self.graph_dict.keys()}

        for key, val in self.graph_dict.items():
            node_map[key].neighbors = [node_map[i] for i in val]

        return node_map[node.val]

    def dfs(self, node):
        if node.val not in self.graph_dict:
            self.graph_dict[node.val] = [n.val for n in node.neighbors]
            
            for node in node.neighbors:
                self.dfs(node)
