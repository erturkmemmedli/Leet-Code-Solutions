# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def __init__(self):
        self.output = deque()
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        self.output.append(root)
        result = []
        while self.output:
            temp = self.output[0]
            self.dfs(to_delete, self.output[0])
            if self.output and temp == self.output[0]:
                result.append(self.output[0])
                self.output.popleft()
        return result
        
    def dfs(self, to_delete, node):
        if node.val in to_delete:
            self.output.popleft()
            if node.left:
                self.output.append(node.left)
            if node.right:
                self.output.append(node.right)
            return
        else:
            if node.left:
                if node.left.val in to_delete:
                    self.output.append(node.left)
                    node.left = None
                else:
                    self.dfs(to_delete, node.left)
            if node.right:
                if node.right.val in to_delete:
                    self.output.append(node.right)
                    node.right = None
                else:
                    self.dfs(to_delete, node.right)
        return node

# Alternative solution

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        candidates = deque([(root, True)])
        output = []

        while candidates:
            node, addable = candidates.popleft()

            if node.val in to_delete:
                if node.left:
                    candidates.append((node.left, True))
                if node.right:
                    candidates.append((node.right, True))

            else:
                if addable:
                    output.append(node)

                if node.left:
                    if node.left.val in to_delete:
                        candidates.append((node.left, True))
                        node.left = None
                    else:
                        candidates.append((node.left, False))
                if node.right:
                    if node.right.val in to_delete:
                        candidates.append((node.right, True))
                        node.right = None
                    else:
                        candidates.append((node.right, False))

        return output
