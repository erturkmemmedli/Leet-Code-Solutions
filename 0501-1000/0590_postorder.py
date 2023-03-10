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
        
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        for child in root.children:
            self.postorder(child)
        self.output.append(root.val)
        return self.output
      
#

class Solution1:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        visited = set()
        stack = [root]
        output = []
        while stack:
            if stack[-1] not in visited:
                visited.add(stack[-1])
                if stack[-1].children:
                    for child in stack[-1].children[::-1]:
                        stack.append(child)
            else:
                output.append(stack[-1].val)
                stack.pop()
        return output
