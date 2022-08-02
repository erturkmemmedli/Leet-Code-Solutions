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
