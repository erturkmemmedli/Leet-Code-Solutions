# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

# Alternative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.index = 0
        return self.recursion(inorder_map, preorder, 0, len(preorder)-1)
        
    def recursion(self, inorder_map, preorder, left, right):
        if left > right:
            return
        val = preorder[self.index]
        self.index += 1
        root = TreeNode(val)   
        mid = inorder_map[val]
        root.left = self.recursion(inorder_map, preorder, left, mid-1)
        root.right = self.recursion(inorder_map, preorder, mid+1, right)
        return root
