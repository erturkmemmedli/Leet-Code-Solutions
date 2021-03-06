"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.output = []
        
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return
        self.output.append(root.val)
        for child in root.children:
            self.preorder(child)
        return self.output

# Alternative solution

class Solution1:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            output.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return output
