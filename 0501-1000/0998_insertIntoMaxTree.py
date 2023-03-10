# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        arr = []
        self.inorder_traversal(root, arr)
        arr.append(val)
        return self.construct_max_tree(arr)
        
    def inorder_traversal(self, node, arr):
        if not node: return
        self.inorder_traversal(node.left, arr)
        arr.append(node.val)
        self.inorder_traversal(node.right, arr)
        
    def construct_max_tree(self, arr):
        stack = []
        for num in arr:
            node = TreeNode(num)
            left = None
            while stack and stack[-1].val < num:
                left = stack.pop()
            node.left = left
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

# Alternative solution

class Solution1:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
