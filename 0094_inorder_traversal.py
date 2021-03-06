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
