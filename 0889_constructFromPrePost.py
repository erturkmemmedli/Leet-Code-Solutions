# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        self.div_and_con(root, preorder[1:], postorder[:-1])
        return root

    def div_and_con(self, root, pre, post):
        if not pre:
            return root
        elif len(pre) == 1:
            root.left = TreeNode(pre[0])
            return root
        elif len(pre) == 2:
            if pre == post:
                root.left = TreeNode(pre[0])
                root.right = TreeNode(pre[1])
            else:
                root.left = TreeNode(pre[0])
                root.left.left = TreeNode(pre[1])
            return root
        if pre[0] == post[-1]:
            root.left = self.div_and_con(TreeNode(pre[0]), pre[1:], post[:-1])
        if pre[0] != post[-1]:
            idx = pre.index(post[-1])
            root.left = self.div_and_con(TreeNode(pre[0]), pre[1:idx], post[:idx-1])
            root.right = self.div_and_con(TreeNode(post[-1]), pre[idx+1:], post[idx:len(post)-1])
        return root

# Alternative solution

class Solution1:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = preorder.index(postorder[-2])
        root.left = self.constructFromPrePost(preorder[1:index], postorder[:index-1])
        root.right = self.constructFromPrePost(preorder[index:], postorder[index-1:-1])
        return root

# Alternative solution

class Solution2:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        preorder_map = {val: i for i, val in enumerate(preorder)}
        self.index = len(postorder)-1
        return self.recursion(preorder_map, postorder, 0, len(preorder)-1)
    
    def recursion(self, preorder_map, postorder, left, right):
        if left > right:
            return
        val = postorder[self.index]
        self.index -= 1
        root = TreeNode(val)
        if left == right:
            return TreeNode(val)
        mid = preorder_map[postorder[self.index]]
        root.right = self.recursion(preorder_map, postorder, mid, right)
        root.left = self.recursion(preorder_map, postorder, left+1, mid-1)
        return root
