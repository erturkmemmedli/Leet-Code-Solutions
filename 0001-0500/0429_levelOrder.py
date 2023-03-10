"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        Q = deque([[root]])
        output = [[root.val]]
        while Q:
            node_list = Q.popleft()
            temp = []
            nodes = []
            for node in node_list:
                for child in node.children:
                    nodes.append(child)
                    temp.append(child.val)
            if temp:
                output.append(temp)
            if nodes:
                Q.append(nodes)
        return output

# Alternative solution

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        levelOrder = []
        while queue:
            levelSize = len(queue)
            level = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                level.append(currentNode.val)
                for node in currentNode.children:
                    queue.append(node)
            levelOrder.append(level)
        return levelOrder
