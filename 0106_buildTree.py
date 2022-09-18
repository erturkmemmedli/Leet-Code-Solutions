# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        val = postorder[-1]
        root = TreeNode(val)
        index = inorder.index(val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

# Alternative solution

class Solution1:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.index = len(postorder)-1
        return self.recursion(inorder_map, postorder, 0, len(postorder)-1)
        
    def recursion(self, inorder_map, postorder, left, right):
        if left > right:
            return
        val = postorder[self.index]
        self.index -= 1
        root = TreeNode(val)
        mid = inorder_map[val]
        root.right = self.recursion(inorder_map, postorder, mid+1, right)
        root.left = self.recursion(inorder_map, postorder, left, mid-1)
        return root
