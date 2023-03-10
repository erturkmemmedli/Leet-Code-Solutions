# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.List = []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        self.inorderTraversal(root.left)
        self.List.append(root.val)
        self.inorderTraversal(root.right)
        return self.List

# Alternative solution

class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.inorder(root, output)
        return output
    
    def inorder(self, node, output):
        if not node: return
        self.inorder(node.left, output)
        output.append(node.val)
        self.inorder(node.right, output)
        return node

# Alternative solution

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorderList = []
        self.inorderDFS(root)
        return self.inorderList
    
    def inorderDFS(self, node):
        if not node:
            return
        self.inorderDFS(node.left)
        self.inorderList.append(node.val)
        self.inorderDFS(node.right)

# Alternative solution

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorderList = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    inorderList.append(node.val)
                else:
                    stack.extend([(node.right, False), (node, True), (node.left, False)])
        return inorderList
