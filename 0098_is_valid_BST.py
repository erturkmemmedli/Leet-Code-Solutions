# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_list = []
        self.inorderTraversal(root, inorder_list)
        for i in range(1, len(inorder_list)):
            if inorder_list[i] <= inorder_list[i-1]:
                return False
        return True
        
    def inorderTraversal(self, root, List):
        if not root: return
        if root.left: self.inorderTraversal(root.left, List)
        List.append(root.val)
        if root.right: self.inorderTraversal(root.right, List)

# Alternative solution

class Solution1:
    def __init__(self):
        self.flag = True
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_list = []
        self.inorderTraversal(root, inorder_list)
        return self.flag
        
    def inorderTraversal(self, root, List):
        if not root: return
        if root.left: self.inorderTraversal(root.left, List)
        List.append(root.val)
        if len(List) > 1 and List[-1] <= List[-2]:
            self.flag = False
        if root.right: self.inorderTraversal(root.right, List)
