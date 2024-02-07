# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.List = []
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.List.append(root.val)
        return self.List

# Alternative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        postorder = []

        while stack:
            node, flag = stack.pop()

            if not node:
                continue
            
            if not flag:
                stack.append((node, not flag))
                stack.append((node.right, flag))
                stack.append((node.left, flag))

            else:
                postorder.append(node.val)
            
        return postorder
